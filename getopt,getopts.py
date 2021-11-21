getopt and getopts
1. 쉘 스크립트에서 getopt
-> getopt명령어를 사용하는 이유
  1. 다양한 입력 값이 존재할 경우 개발자와 사용자의 편의를 위해서
  2. 스크립트를 보다 체계적으로 관리할 수 있다.
 
-> getopt의 특징
 기본적으로 short, long옵션을 지원
 옵션 인수를 가질 경우, 문자를 사용하는 것은 getopts builtin 명령과 동일하다.
short 옵션 지정은 -o, long 옵션 지정은 -l
 getopt -o a:bc -> ':' 에 따라서 옵션 -a는 옵션 인수를 갖는다.
 ':' 에 따라서 옵션 --path와 --name은 옵션 인수를 갖는다.
 getopt -l help,path:,name: ->':' 에 따라서 옵션 --path와 --name은 옵션 인수를 갖는다.
 명령 마지막에는 -- 을 붙인다. 
