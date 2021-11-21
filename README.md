# TEST1_20203145
20203145

1. getopt와 getopts 

(1)getopt

-> getopts 명령어 : 옵션 해석 작업을 쉽게 도와주는 명령어 이다.  getopts 명령은 short 옵션을 처리한다.
-> getopts 명령에서 사용되는 optstring, varname 과 OPTIND가 있다. 
   --->shell 이 처음 실행되면 OPTIND 값은 1 을 가리키고 getopts 명령이 실행될 때마다 다음 옵션의 index 값을 가리킨다.
-> 옵션은 옵션인수를 가질 수 있는데, 이때 옵션 스트링에서 해당 옵션 문자 뒤에 : 을 붙인다. 그러면 getopts 명령은 옵션인수 값를 OPTARG 변수에 설정해 준다.
-> getopts 명령은 error reporting 과 관련해서 다음과 같은 두 개의 모드를 제공한다.
   ----> default 는 verbose mode 인데 기본적으로 옵션과 관련된 오류메시지가 표시되므로 스크립트를 배포할 때는 잘 사용하지 않고 대신 silent mode 를 이용한다. 
-> silent mode 를 설정하기 위해서는 옵션 스트링의 맨 앞부분에 : 문자를 추가해준다.
-> OPTIND, OPTARG 변수는 local 변수가 아니므로 필요할 경우 함수 내에서 local 로 설정해 사용해야 합니다.
-> Long 옵션처리
   ---->  getopts 명령으로 short, long 옵션을 동시에 처리하는 것은 어려우므로 먼저 long 옵션을 처리하고 난후 나머지 short 옵션만 정리하여 getopts 에 넘겨주면 이전과 동일하게 short 옵션을 처리할 수 있다.
   ----> long 옵션을 @ 에서 삭제하는 방법은 while 문을 이용해 인수들을 하나씩 처리하면서 long 옵션이 아닐 경우 특정 변수에 계속해서 append 하는 것입니다. 마지막으로 long 옵션이 제거된 변수를 이용해 set 명령으로 다시 @ 값을 설정한다.
   
(2)getopts

-> "/usr/bin/getopt" 에 위치한 외부 명령dlek.
-> 기본적으로 short, long 옵션을 모두 지원합니다. 옵션 인수를 가질 경우 : 문자를 사용하는 것은 getopts builtin 명령과 동일gkek.
-> short 옵션 지정은 -o 옵션으로 합니다. ':' 에 따라서 옵션 -a 는 옵션 인수를 갖습니다. => getopt -o a:bc
-> long 옵션 지정은 -l 옵션으로 하고 옵션명은 ',' 로 구분합니다. ':' 에 따라서 옵션 --path 와 --name 은 옵션 인수를 갖습니다.
   ---->명령 라인에서 옵션 인수 사용은 "--name foo" 또는 "--name=foo" 두 가지 모두 가능합니다. => getopt -l help,path:,name: 
-> 명령 마지막에는 -- 와 함께 "$@" 를 붙인다.
-> 설정하지 않은 옵션이 사용되거나 옵션 인수가 빠질 경우 오류메시지를 출력해준다.
-> getopt 명령의 특징은 사용자가 입력한 옵션들을 case 문에서 사용하기 좋게 정렬해준다.
-> getopts builtin 명령의 경우 옵션들 중간에 파일명이 온다거나 하면 이후의 옵션은 옵션으로 인식이 되지 않는데 getopt 명령의 경우는 올바르게 구분하여 정렬해 준다.
->다양한 입력 값이 존재할 경우 사용자와 개발자의 편의를 보장해주고, 스크립트를 보다 체계적으로 관리할 수 있기 때문에 사용한다.
