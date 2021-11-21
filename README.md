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
-> 다양한 입력 값이 존재할 경우 사용자와 개발자의 편의를 보장해주고, 스크립트를 보다 체계적으로 관리할 수 있기 때문에 사용한다.

2. sed 및 awk명령어 

(1) sed (streamlined editor)
 -> 명령행에서 파일을 인자로 받아 명령어를 통해 작업한 후 결과를 화면으로 확인 하는 방식
 -> sed편집기는 원본ㅇㄹ 손상하지 않는다. 쉘 리다이렉션을 이용해 편집결과를 저장하기 전까지는 파일에 아무런 변경도 가하지 않는다.
 -> 출력된 결과가 원본과 다르더라도 원본에 손해가 없다.
 -> sed명령어는 동작시 내부적으로 두개의 워크스페이스를 사용하는데, 이 두 버퍼를 패턴스페이스와 홀드 스페이스라고 한다. (내가 현재 담고있는 정보)
    ----> 패턴 스페이스는 sed가 파일을 라인단위로 읽을 때 그 읽힌 라인이 저장되는 임시공간
    ----> 홀드 스페이스는 패턴 스페이스와 달리 원할 때 이전 행을 불러와서 사용할 수 있는 버퍼이다. 
    
 -> "sed -n '*,*p employees'" => 컴마는 주소범위, p는 출력을 의미한다.
 -> "sed -n -e '1p' -e '*,$p employees'" => 여러개의 편집 명령 실행 시 -e 옵션을 쓴다.
 -> "sed -n '/^a037185a/p' employees" => a037185a로 시작(특정단어로 시작하는 행들만 추출시에는 ^제외) 
     ----> '^'는 메타문자로 '시작'을 의미한다.특정단어 포함하는 행들을 뽑을 떄에는 없이 검색한다.
     
 -> "sed '/^$/d' employees" => employees파일에서 빈 라인들을 지운 후 내용을 출력한다.
 -> "sed '/^$/d' employees" > new employees => employees파일에서 빈 라인들을 삭제한 후 결과를 new_employees라는 파일명으로 저장
 -> "sed '/^ *$/d' employees" > new employees => employees파일에서 빈 라인들이나 공백으로 채워진 행을 삭제한 후 new_employees라는 파일명으로 저장
 
 -> "sed 's/a037185a/DEVELOPER/g' employees" s는 치환할 때 사용하는 커맨트, 같이 쓰는 g플래그는 치환이 행에서 전체를 대상으로 이루어진다는 뜻
 -> "sed 's/a037185a/DEVELOPER/g' employees"
 -> "sed 's/a037185a/DEVELOPER/gi' employees" i는 변경대상 단어를 찾을 때 대소문자를 무시한다는 플래그이다.
