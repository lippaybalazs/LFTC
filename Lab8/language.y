%{
    #include <stdio.h>
    #include <stdlib.h>
    #define YYDEBUG 1

    #define TYPE_INT 1
    #define TYPE_STR 2

    double stack[20];
    int stack_pointer;

    void push (double x)
    {
        stack[stack_pointer++] = x;
    }  

    void pop ()
    {
        return stack[stack_pointer--];
    }
%}

%token ARITMETIC_OPERATOR
%token COMPARISON_OPERATOR
%token LOGICAL_OPERATOR
%token NOT
%token IF
%token ELSE
%token WHILE
%token INT
%token LIST
%token STR
%token PRINT
%token INPUT
%token CONSTANT_INT
%token CONSTANT_STR
%token IDENTIFIER

%%

program:                compstmt
                        ;
compstmt:               stmt '\n'
                        | stmt '\n' compstmt
                        ;
stmt:                   simplstmt
                        | structstmt
                        ;
simplstmt:              assignstmt
                        | declstmt
                        | printstmt
                        | arithmstmt
                        ;
arithmstmt:             IDENTIFIER ARITMETIC_OPERATOR expression
                        ;
printstmt:              PRINT '(' expression ')'
                        ;
declstmt:               IDENTIFIER ':' type '=' expression
                        ;
assignstmt:             IDENTIFIER '=' expression
                        ;
type:                   INT
                        | STR
                        | LIST
                        ;

expression:             conversionexpression
                        | readexpression
                        | listexpression
                        | constantexpression
                        | IDENTIFIER
                        ;
listexpression:         '[' listmiddle ']'
                        ;
listmiddle:             expression
                        | expression ',' listmiddle
                        ;
readexpression:         INPUT
                        ;
conversionexpression:   INT '(' expression ')'
                        | STR '(' expression ')'
                        ;
constantexpression:     CONSTANT_INT
                        | CONSTANT_STR
                        ;
structstmt:             compstmt
                        | whilestmt
                        | ifstmt
                        ;
ifstmt:                 IF condition ':' '\n' compstmt
                        | IF condition ':' '\n' compstmt ELSE ':' '\n' compstmt
                        ;
whilestmt:              WHILE condition ':' '\n' compstmt
                        ;
logicalexpression:      NOT expression COMPARISON_OPERATOR expression
                        | expression COMPARISON_OPERATOR expression
                        ;
condition:              logicalexpression
                        | NOT logicalexpression
                        | logicalexpression LOGICAL_OPERATOR condition
                        ;

%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}