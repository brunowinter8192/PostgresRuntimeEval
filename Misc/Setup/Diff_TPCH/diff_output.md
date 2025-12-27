diff -Nur --exclude=*.o --exclude=*.tbl --exclude=dbgen --exclude=qgen --exclude=.DS_Store ORIGINAL/dbgen/bm_utils.c MODIFIED/dbgen/bm_utils.c
--- ORIGINAL/dbgen/bm_utils.c	2021-06-09 09:41:24
+++ MODIFIED/dbgen/bm_utils.c	2025-09-25 00:25:32
@@ -67,9 +67,13 @@
 #endif            /* HP */
 #include <ctype.h>
 #include <math.h>
+#ifdef __APPLE__
+#include <stdlib.h>
+#else
 #ifndef _POSIX_SOURCE
 #include <malloc.h>
 #endif /* POSIX_SOURCE */
+#endif /* __APPLE__ */
 #include <fcntl.h>
 #include <sys/types.h>
 #include <sys/stat.h>
diff -Nur --exclude=*.o --exclude=*.tbl --exclude=dbgen --exclude=qgen --exclude=.DS_Store ORIGINAL/dbgen/makefile.suite MODIFIED/dbgen/makefile.suite
--- ORIGINAL/dbgen/makefile.suite	2021-06-09 09:41:24
+++ MODIFIED/dbgen/makefile.suite	2025-09-25 02:05:29
@@ -100,15 +100,15 @@
 ################
 ## CHANGE NAME OF ANSI COMPILER HERE
 ################
-CC      = 
+CC      = gcc
 # Current values for DATABASE are: INFORMIX, DB2, TDAT (Teradata)
-#                                  SQLSERVER, SYBASE, ORACLE, VECTORWISE
+#                                  SQLSERVER, SYBASE, ORACLE, VECTORWISE, POSTGRESQL
 # Current values for MACHINE are:  ATT, DOS, HP, IBM, ICL, MVS, 
 #                                  SGI, SUN, U2200, VMS, LINUX, WIN32 
 # Current values for WORKLOAD are:  TPCH
-DATABASE= 
-MACHINE = 
-WORKLOAD = 
+DATABASE = POSTGRESQL
+MACHINE = LINUX
+WORKLOAD = TPCH 
 #
 CFLAGS	= -g -DDBNAME=\"dss\" -D$(MACHINE) -D$(DATABASE) -D$(WORKLOAD) -DRNG_TEST -D_FILE_OFFSET_BITS=64 
 LDFLAGS = -O
diff -Nur --exclude=*.o --exclude=*.tbl --exclude=dbgen --exclude=qgen --exclude=.DS_Store ORIGINAL/dbgen/qgen.c MODIFIED/dbgen/qgen.c
--- ORIGINAL/dbgen/qgen.c	2021-06-09 09:41:24
+++ MODIFIED/dbgen/qgen.c	2025-09-25 15:59:20
@@ -28,6 +28,9 @@
 #define DECLARER
 
 #include <stdio.h>
+#ifdef POSTGRESQL
+#include <stdarg.h>
+#endif
 #include <string.h>
 #if (defined(_POSIX_)||!defined(WIN32))
 #include <unistd.h>
@@ -54,6 +57,7 @@
 int process_options PROTO((int cnt, char **args));
 int setup PROTO((void));
 void qsub PROTO((char *qtag, int flags));
+void postgresql_fix_intervals PROTO((char *line));
 
 
 
@@ -125,6 +129,192 @@
 }
 
 /*
+ * FUNCTION postgresql_fix_intervals(line)
+ *
+ * Fix PostgreSQL interval syntax
+ */
+void
+postgresql_fix_intervals(char *line)
+{
+    char *pos;
+    char temp_buffer[512];
+    
+    if ((pos = strstr(line, "interval '")) != NULL)
+    {
+        char *day_pos = strstr(pos, "' day (3)");
+        if (day_pos != NULL)
+        {
+            pos[0] = 'I'; pos[1] = 'N'; pos[2] = 'T'; pos[3] = 'E'; 
+            pos[4] = 'R'; pos[5] = 'V'; pos[6] = 'A'; pos[7] = 'L';
+            
+            char *num_start = pos + 9;
+            while (*num_start == ' ') num_start++;
+            char *num_end = num_start;
+            while (*num_end >= '0' && *num_end <= '9') num_end++;
+            
+            int num = atoi(num_start);
+            strcpy(temp_buffer, day_pos + 9);
+            strcpy(day_pos, (num == 1) ? " day'" : " days'");
+            strcat(day_pos, temp_buffer);
+        }
+        
+        char *year_pos = strstr(pos, "' year");
+        if (year_pos != NULL)
+        {
+            pos[0] = 'I'; pos[1] = 'N'; pos[2] = 'T'; pos[3] = 'E'; 
+            pos[4] = 'R'; pos[5] = 'V'; pos[6] = 'A'; pos[7] = 'L';
+            
+            char *num_start = pos + 9;
+            while (*num_start == ' ') num_start++;
+            int num = atoi(num_start);
+            
+            strcpy(temp_buffer, year_pos + 6);
+            strcpy(year_pos, (num == 1) ? " year'" : " years'");
+            strcat(year_pos, temp_buffer);
+        }
+        
+        char *month_pos = strstr(pos, "' month");
+        if (month_pos != NULL)
+        {
+            pos[0] = 'I'; pos[1] = 'N'; pos[2] = 'T'; pos[3] = 'E'; 
+            pos[4] = 'R'; pos[5] = 'V'; pos[6] = 'A'; pos[7] = 'L';
+            
+            char *num_start = pos + 9;
+            while (*num_start == ' ') num_start++;
+            int num = atoi(num_start);
+            
+            strcpy(temp_buffer, month_pos + 7);
+            strcpy(month_pos, (num == 1) ? " month'" : " months'");
+            strcat(month_pos, temp_buffer);
+        }
+    }
+    
+    if ((pos = strstr(line, "date '")) != NULL)
+    {
+        pos[0] = 'D'; pos[1] = 'A'; pos[2] = 'T'; pos[3] = 'E';
+    }
+}
+
+#ifdef POSTGRESQL
+/*
+ * Pre-scan template file to detect :n directive (LIMIT clause)
+ * Returns: limit value if found, 0 otherwise
+ */
+static int detect_limit_directive(const char *qpath, int flags)
+{
+    FILE *fp;
+    char line[BUFSIZ];
+    int limit = 0;
+    
+    fp = fopen(qpath, "r");
+    if (!fp) return 0;
+    
+    while (fgets(line, BUFSIZ, fp) != NULL)
+    {
+        char *ptr = line;
+        
+        /* Skip comments unless COMMENT flag set */
+        if (!(flags & COMMENT) && strstr(line, "--") == line)
+            continue;
+            
+        /* Look for :n directive */
+        if ((ptr = strchr(line, VTAG)) != NULL)
+        {
+            ptr++;
+            if (*ptr == 'n' || *ptr == 'N')
+            {
+                ptr++;
+                while (isspace(*ptr)) ptr++;
+                if (isdigit(*ptr))
+                {
+                    limit = atoi(ptr);
+                    break;
+                }
+            }
+        }
+    }
+    
+    fclose(fp);
+    return limit;
+}
+
+/*
+ * Buffer management for PostgreSQL LIMIT handling
+ */
+static char *query_buffer = NULL;
+static size_t buffer_size = 0;
+static size_t buffer_pos = 0;
+
+static void buffer_init(void)
+{
+    buffer_size = BUFSIZ * 10; /* Start with 10x BUFSIZ */
+    query_buffer = malloc(buffer_size);
+    buffer_pos = 0;
+    if (query_buffer) query_buffer[0] = '\0';
+}
+
+static void buffer_append(const char *format, ...)
+{
+    va_list args;
+    size_t needed;
+    
+    if (!query_buffer) buffer_init();
+    
+    va_start(args, format);
+    needed = vsnprintf(NULL, 0, format, args) + 1;
+    va_end(args);
+    
+    /* Grow buffer if needed */
+    if (buffer_pos + needed > buffer_size)
+    {
+        buffer_size *= 2;
+        query_buffer = realloc(query_buffer, buffer_size);
+    }
+    
+    va_start(args, format);
+    vsnprintf(query_buffer + buffer_pos, buffer_size - buffer_pos, format, args);
+    va_end(args);
+    
+    buffer_pos += needed - 1;
+}
+
+static void buffer_flush_with_limit(FILE *fp, int limit)
+{
+    if (!query_buffer) return;
+    
+    if (limit > 0)
+    {
+        /* Find last semicolon */
+        char *last_semi = strrchr(query_buffer, ';');
+        if (last_semi)
+        {
+            /* Insert LIMIT before semicolon */
+            *last_semi = '\0';
+            fprintf(fp, "%s\nLIMIT %d;\n", query_buffer, limit);
+            /* Output any text after semicolon */
+            if (*(last_semi + 1))
+                fprintf(fp, "%s", last_semi + 1);
+        }
+        else
+        {
+            /* No semicolon found - add LIMIT at end */
+            fprintf(fp, "%s\nLIMIT %d;\n", query_buffer, limit);
+        }
+    }
+    else
+    {
+        /* No LIMIT needed */
+        fprintf(fp, "%s", query_buffer);
+    }
+    
+    free(query_buffer);
+    query_buffer = NULL;
+    buffer_size = 0;
+    buffer_pos = 0;
+}
+#endif
+
+/*
  * FUNCTION qsub(char *qtag, int flags)
  *
  * based on the settings of flags, and the template file $QDIR/qtag.sql
@@ -154,7 +344,18 @@
     *mark,
     *qroot = NULL;
 
+#ifdef POSTGRESQL
+static int query_limit_value = 0;
+#endif
+
     qnum = atoi(qtag);
+    
+#ifdef POSTGRESQL
+    /* Initialize buffer for query */
+    buffer_init();
+    query_limit_value = 0;
+#endif
+
     if (line == NULL)
         {
         line = malloc(BUFSIZ);
@@ -166,73 +367,134 @@
     qroot = env_config(QDIR_TAG, QDIR_DFLT);
     sprintf(qpath, "%s%c%s.sql", 
 		qroot, PATH_SEP, qtag);
+    
+#ifdef POSTGRESQL
+    /* Pre-scan for :n directive */
+    query_limit_value = detect_limit_directive(qpath, flags);
+    if (query_limit_value < 0) query_limit_value = 0;  /* Safety check */
+#endif
+    
     qfp = fopen(qpath, "r");
     OPEN_CHECK(qfp, qpath);
 
     rowcnt = rowcnt_dflt[qnum];
     varsub(qnum, 0, flags); /* set the variables */
-    if (flags & DFLT_NUM)
+    
+#ifdef POSTGRESQL
+    /* If default rowcount and we have detected a limit from pre-scan */
+    if (flags & DFLT_NUM && rowcnt > 0 && query_limit_value == 0)
+        query_limit_value = rowcnt;
+#else
+    if (flags & DFLT_NUM && rowcnt > 0)
         fprintf(ofp, SET_ROWCOUNT, rowcnt);
+#endif
+
     while (fgets(line, BUFSIZ, qfp) != NULL)
         {
         if (!(flags & COMMENT))
             strip_comments(line);
+#ifdef POSTGRESQL
+        postgresql_fix_intervals(line);
+#endif
         mark = line;
         while ((cptr = strchr(mark, VTAG)) != NULL)
             {
             *cptr = '\0';
-             cptr++;
+            cptr++;
+#ifdef POSTGRESQL
+            buffer_append("%s", mark);
+#else
             fprintf(ofp,"%s", mark);
+#endif
             switch(*cptr)
                 {
                 case 'b':
                 case 'B':
                     if (!(flags & ANSI))
+#ifdef POSTGRESQL
+                        buffer_append("%s\n", START_TRAN);
+#else
                         fprintf(ofp,"%s\n", START_TRAN);
+#endif
                     cptr++;
                     break;
                 case 'c':
                 case 'C':
                     if (flags & DBASE)
+#ifdef POSTGRESQL
+                        buffer_append(SET_DBASE, db_name);
+#else
                         fprintf(ofp, SET_DBASE, db_name);
+#endif
                     cptr++;
                     break;
                 case 'e':
                 case 'E':
                     if (!(flags & ANSI))
+#ifdef POSTGRESQL
+                        buffer_append("%s\n", END_TRAN);
+#else
                         fprintf(ofp,"%s\n", END_TRAN);
+#endif
                     cptr++;
                     break;
                 case 'n':
                 case 'N':
+#ifdef POSTGRESQL
+                    /* Already handled in pre-scan, skip to next */
                     if (!(flags & DFLT_NUM))
+                    {
+                        cptr++;
+                        while (isdigit(*cptr) || *cptr == ' ') cptr++;
+                    }
+#else
+                    if (!(flags & DFLT_NUM))
                         {
                         rowcnt=atoi(++cptr);
                         while (isdigit(*cptr) || *cptr == ' ') cptr++;
-                        fprintf(ofp, SET_ROWCOUNT, rowcnt);
+                        if (rowcnt > 0)
+                            fprintf(ofp, SET_ROWCOUNT, rowcnt);
                         }
+#endif
                     continue;
                 case 'o':
                 case 'O':
                     if (flags & OUTPUT)
+#ifdef POSTGRESQL
+                        buffer_append("%s '%s/%s.%d'", SET_OUTPUT, osuff, 
+                            qtag, (snum < 0)?0:snum);
+#else
                         fprintf(ofp,"%s '%s/%s.%d'", SET_OUTPUT, osuff, 
                             qtag, (snum < 0)?0:snum);
+#endif
                     cptr++;
                     break;
                 case 'q':
                 case 'Q':
+#ifdef POSTGRESQL
+                    buffer_append("%s", qtag);
+#else
                     fprintf(ofp,"%s", qtag);
+#endif
                     cptr++;
                     break;
                 case 's':
                 case 'S':
+#ifdef POSTGRESQL
+                    buffer_append("%d", (snum < 0)?0:snum);
+#else
                     fprintf(ofp,"%d", (snum < 0)?0:snum);
+#endif
                     cptr++;
                     break;
                 case 'X':
                 case 'x':
                     if (flags & EXPLAIN)
+#ifdef POSTGRESQL
+                        buffer_append("%s\n", GEN_QUERY_PLAN);
+#else
                         fprintf(ofp, "%s\n", GEN_QUERY_PLAN);
+#endif
                     cptr++;
                     break;
 		case '1':
@@ -244,7 +506,26 @@
 		case '7':
 		case '8':
 		case '9':
+#ifdef POSTGRESQL
+                    /* Use temporary file for varsub output, then read it into buffer */
+                    {
+                        FILE *tmp_fp = tmpfile();
+                        FILE *saved_ofp = ofp;
+                        char tmp_buf[BUFSIZ];
+                        
+                        ofp = tmp_fp;
+                        varsub(qnum, atoi(cptr), flags & DFLT);
+                        rewind(tmp_fp);
+                        
+                        while (fgets(tmp_buf, BUFSIZ, tmp_fp) != NULL)
+                            buffer_append("%s", tmp_buf);
+                        
+                        fclose(tmp_fp);
+                        ofp = saved_ofp;
+                    }
+#else
                     varsub(qnum, atoi(cptr), flags & DFLT);
+#endif
                     while (isdigit(*++cptr));
                     break;
                 default:
@@ -255,8 +536,20 @@
                 }
             mark=cptr;
             }
+            
+        /* Output remaining part of line */
+#ifdef POSTGRESQL
+        buffer_append("%s", mark);
+#else
         fprintf(ofp,"%s", mark);
+#endif
         }
+    
+#ifdef POSTGRESQL
+    /* Output complete query with LIMIT if needed */
+    buffer_flush_with_limit(ofp, query_limit_value);
+#endif
+    
     fclose(qfp);
     fflush(stdout);
     return;
diff -Nur --exclude=*.o --exclude=*.tbl --exclude=dbgen --exclude=qgen --exclude=.DS_Store ORIGINAL/dbgen/tpcd.h MODIFIED/dbgen/tpcd.h
--- ORIGINAL/dbgen/tpcd.h	2021-06-09 09:41:24
+++ MODIFIED/dbgen/tpcd.h	2025-09-25 00:21:31
@@ -49,6 +49,15 @@
 /*
  * database portability defines
  */
+#ifdef POSTGRESQL
+#define GEN_QUERY_PLAN  "explain"
+#define START_TRAN      "start transaction"
+#define END_TRAN        "commit;"
+#define SET_OUTPUT      ""
+#define SET_ROWCOUNT    "limit %d;\n"
+#define SET_DBASE       ""
+#endif /* POSTGRESQL */
+
 #ifdef VECTORWISE
 #define GEN_QUERY_PLAN  "EXPLAIN"
 #define START_TRAN      ""
diff -Nur --exclude=*.o --exclude=*.tbl --exclude=dbgen --exclude=qgen --exclude=.DS_Store ORIGINAL/dbgen/varsub.c MODIFIED/dbgen/varsub.c
--- ORIGINAL/dbgen/varsub.c	2021-06-09 09:41:24
+++ MODIFIED/dbgen/varsub.c	2025-09-25 00:37:47
@@ -40,9 +40,13 @@
 *
 */
 #include <stdio.h>
+#ifdef __APPLE__
+#include <stdlib.h>
+#else
 #ifndef _POSIX_SOURCE
 #include <malloc.h>
 #endif /* POSIX_SOURCE */
+#endif /* __APPLE__ */
 #if (defined(_POSIX_)||!defined(WIN32))
 #include <unistd.h>
 #endif /* WIN32 */
