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
 설정하지 않은 옵션이 사용되거나 옵션 인수가 빠질경우 오류메세지를 출력해준다. 
 사용자가 입력한 옵션들을 case문에서 사용하기 좋게 정렬해준다.
2. 쉘 스크립트에서 getopts
 -> 옵션 해석 작업을 도와주는 명령어!
 -> 옵션에는 short, long이 있는데 getopts명령어는 short 옵션을 처리한다.
 -> getopts 명령에서 사용되는 optstring, varname, 1
 -> shell이 처음 실행되면 1 값은 1을 가리키고, getopts 명령이 실행될 떄 마다 다음 옵션의 index값을 가리킨다.
 -> shell이 처음 실행되면 '1' 값은 1을 가리키고, getopts 명령이 실행될 떄 마다 다음 옵션의 index값을 가리킨다.
  -----> '1' = OPTIND
 -> 옵션은 옵션인수를 가질 수 있는데, 이때 옵션 스트링에서 해당 옵션 문자 뒤에 ':'을 붙인다. 그러면 getopts명령은 옵션인수 값을 OPTARG 변수에 설정해준다. 
 -> getopts 명령은 error reporting 과 관련해서 Verbose mode와 Silent mode
  ----> default는 verbose mode인데 기본적으로 옵션과 관련된 오류메세지만 표시 되므로 스크립트를 배포할 때 잘 사용되지 않고 Silent mode를 이용한다.
 -> silent mode를 사용하기 위해서는 옵션 스트링의 맨 앞부분에 : 문자를 추가해준다.
