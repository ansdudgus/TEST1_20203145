# TEST1_20203145
20203145

(1)getopts

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
-> 기본적으로 short, long 옵션을 모두 지원. 옵션 인수를 가질 경우 : 문자를 사용하는 것은 getopts builtin 명령과 동일.
-> getopts option 넣기. while + getopts, 옵션은 $opt 에 loop 하나씩 들어간다.
-> short 옵션 지정은 -o 옵션으로 합니다. ':' 에 따라서 옵션 -a 는 옵션 인수를 갖습니다. => getopt -o a:bc
-> long 옵션 지정은 -l 옵션으로 하고 옵션명은 ',' 로 구분합니다. ':' 에 따라서 옵션 --path 와 --name 은 옵션 인수를 갖습니다.
   ---->명령 라인에서 옵션 인수 사용은 "--name foo" 또는 "--name=foo" 두 가지 모두 가능합니다. => getopt -l help,path:,name: 
-> 명령 마지막에는 -- 와 함께 "$@" 를 붙인다.
-> 설정하지 않은 옵션이 사용되거나 옵션 인수가 빠질 경우 오류메시지를 출력해준다.
-> getopt 명령의 특징은 사용자가 입력한 옵션들을 case 문에서 사용하기 좋게 정렬해준다.
-> getopts builtin 명령의 경우 옵션들 중간에 파일명이 온다거나 하면 이후의 옵션은 옵션으로 인식이 되지 않는데 getopt 명령의 경우는 올바르게 구분하여 정렬해 준다.
-> 다양한 입력 값이 존재할 경우 사용자와 개발자의 편의를 보장해주고, 스크립트를 보다 체계적으로 관리할 수 있기 때문에 사용한다.

(3) sed (streamlined editor)
 -> 명령행에서 파일을 인자로 받아 명령어를 통해 작업한 후 결과를 화면으로 확인 하는 방식
 -> sed편집기는 원본ㅇㄹ 손상하지 않는다. 쉘 리다이렉션을 이용해 편집결과를 저장하기 전까지는 파일에 아무런 변경도 가하지 않는다.
 -> 출력된 결과가 원본과 다르더라도 원본에 손해가 없다.
 -> sed명령어는 동작시 내부적으로 두개의 워크스페이스를 사용하는데, 이 두 버퍼를 패턴스페이스와 홀드 스페이스라고 한다. (내가 현재 담고있는 정보)
    ----> 패턴 스페이스는 sed가 파일을 라인단위로 읽을 때 그 읽힌 라인이 저장되는 임시공간
    ----> 홀드 스페이스는 패턴 스페이스와 달리 원할 때 이전 행을 불러와서 사용할 수 있는 버퍼이다. 
    
 -> "sed -n '*,*p employees'" => 컴마는 주소범위, p는 출력을 의미한다. -n은 자동 출력을 하지 않게 해준다.
 -> "sed -n -e '1p' -e '*,$p employees'" => 여러개의 편집 명령 실행 시 -e 옵션을 쓴다.
 -> "sed -n '/^a037185a/p' employees" => a037185a로 시작(특정단어로 시작하는 행들만 추출시에는 ^제외) 
     ----> '^'는 메타문자로 '시작'을 의미한다.특정단어 포함하는 행들을 뽑을 떄에는 없이 검색한다.
 -> "sed -n -e '1p' -e '8,$p'" => e 옵션을 이용해서 여러개 사용하여 command를 준다.   
 -> "sed -n -e '2,6d' -e '1,$p'" =>  2~6번째 줄을 삭제하고 나머지 모든 내용을 출력
 -> "sed '/^$/d' employees" => employees파일에서 빈 라인들을 지운 후 내용을 출력한다.
 -> "sed '/^$/d' employees" > new employees => employees파일에서 빈 라인들을 삭제한 후 결과를 new_employees라는 파일명으로 저장
 -> "sed '/^ *$/d' employees" > new employees => employees파일에서 빈 라인들이나 공백으로 채워진 행을 삭제한 후 new_employees라는 파일명으로 저장
 
 -> "sed 's/a037185a/DEVELOPER/g' employees" s는 치환할 때 사용하는 커맨트, 같이 쓰는 g플래그는 치환이 행에서 전체를 대상으로 이루어진다는 뜻
 -> "sed 's/a037185a/DEVELOPER/g' employees"
 -> "sed 's/a037185a/DEVELOPER/gi' employees" i는 변경대상 단어를 찾을 때 대소문자를 무시한다는 플래그이다.
 -> "sed -n -e 's/^let/LET/gi' -e '1,$p'" let_it_go.txt => Let으로 시작하는 줄의 첫 Let를 LET으로 바꾼다.
 -> "sed -n -e 's/anyway.$/ANYWAY/gi' -e '1,$p' let_it_go.txt" => 끝나는 문자열은 끝에 $를 붙여줘서 검색하면 됩니다. Anyway. 으로 끝나는 줄의 Anyway를 대문자로 바꾸려면 아래와 같은 command를 사용하면 된다.

-> 문자열을 추가하는 방법에는 두 가지 정도가 존재한다. 해당 문자열 아래에 추가하느냐(Append) 아니면 이 전 줄에 삽입하느냐(Insert)가 있는데, 기본적인 형식은 아래의 command처럼 사용한다.
  /찾을 문자열/a\다음 출에 추가할 문자열
  /찾을 문자열/i\위에 삽입할 문자열
-> "sed -n -e '/^Let/c\Let it go X2' -e '1,$p' let_it_go.txt" => ^를 사용하여 Let으로 시작하는 줄들을 찾고 c 커맨드로 바꿔질 줄 내용을 입력.

-> [sed 명령어의 또다른 기능]
sed명령어의 -f(file)선택자를 사용하면 명령어를 일일이 키보드에서 입력하지 않고 하나의 파일에 기억시켜 놓고 사용할 수도 있다.
     "# sed -f command.file in.file"
여러 개의 명령어를 연속적으로 자주 사용할 때 이 명령어 파일이 유용하게 사용된다.
예를 들어 다음과 같은 복수 개의 명령어가 파일에 기억되어 있는 경우는
     "# vi command.file"
       s/hello/goodbye
       s/good/bad
  다음과 같은 명령어를 입력하면 다음과 같이 출력된다.
     "# echo "1234hello5678" | sed -f command.file"
       => 1234badbye5678

(4) awk
 -> 파일로부터 레코드(record)를 선택하고, 선택된 레코드에 포함된 값을 조작하거나 데이터화하는 것을 목적으로 사용한다.
     ----> awk 명령의 입력으로 지정된 파일로부터 데이터를 분류한 다음, 분류된 텍스트 데이터를 바탕으로 패턴 매칭 여부를 검사하거나 데이터 조작 및 연산 등의 액션을 수행하고, 그 결과를 출력하는 기능을 수행
 -> awk는 "awk programming language"라는 프로그래밍 언어로 작성된 프로그램을 실행한다.
 -> awk는 기본적으로 입력 데이터를 라인(line) 단위의 레코드(Record)로 인식한다. 그리고 각 레코드에 들어 있는 텍스트는 공백 문자(space, tab)로 구분된 필드(Field)들로 분류되는데요. 이렇게 식별된 레코드 및 필드의 값들은 awk 프로그램에 의해 패턴 매칭 및 다양한 액션의 파라미터로 사용한다
 -> awk 명령어 옵션
   awk [OPTION...] [awk program] [ARGUMENT...]
      OPTION
        -F        : 필드 구분 문자 지정.
        -f        : awk program 파일 경로 지정.
        -v        : awk program에서 사용될 특정 variable값 지정.
      awk program
        -f 옵션이 사용되지 않은 경우, awk가 실행할 awk program 코드 지정.
      ARGUMENT
        입력 파일 지정 또는 variable 값 지정.
 -> awk 명령에서 awk program을 풀어쓰면 => awk [OPTION...] 'pattern { action }' [ARGUMENT...]
      ----> pattern과 action은 모두 생략이 가능한데, pattern을 생략하는 경우는 "모든 레코드"가 적용되고, action을 생략하면 "print"가 적용후 실행

 -> pattern과 action에 작성되는 awk program 코드에는 다양한 표현식, 변수, 함수 등이 사용됩니다. 이 중 가장 중요한 변수는 레코드와 필드를 나타내는 변수인데, 하나의 레코드는 $0, 레코드에 포함된 각 필드는 그 순서대로 $1, $2, ..., $n 으로 지칭한다.     
      ----> " awk 'length($0) > 10 { print $3, $4, $5} ' ./file.txt"
 
  -> 패턴 중에 "BEGIN" 과 "END" 라고 하는 특별한 패턴이 존재하는데요, awk가 BEGIN 패턴을 식별하면 입력 데이터로부터 첫 번째 레코드를 처리하기 전에 "BEGIN"에 지정된 액션을 실행합니다. 그리고 "END" 패턴은 "BEGIN"과 반대로, 모든 레코드를 처리한 다음 "END"에 지정된 액션을 실행한다.
      ----> " awk 'BEGIN { print "TITLE : Field value 1,2"} {print $1, $2} END {print "Finished"}' file.txt"
      
  -> "awk '{ print }' ./file.txt" => file.txt의 전체 파일 내용 출력.
  -> "awk '{ print $2 }' ./file.txt " => "print $n" 액션을 통해 n번째 필드 값을 출력할 수 있습니다. 참고로, "$0"은 전체 레코드를 나타내는 변수
  -> "awk '{print "no:"$1, "user:"$2}' ./file.txt" => 필드 값에 임의 문자열을 같이 출력
  -> "awk '/[2-3]0/' ./file.txt" => 지정된 문자열을 포함하는 레코드만 출력. awk의 패턴에 정규 표현식(Regular Expression)을 사용하여 문자열 패턴을 검사할 수 있다. 이 때, 정규 표현식은 "/regex/" 형태로 지정할 수 있다.
  -> "awk '$3 > 70 { print $0 }' ./file.txt " => awk program language의 표현식을 사용하여, 유효한 레코드를 위한 필드 값을 비교하여 선택된 레코드만 출력할 수 있다.
  -> "awk '{sum += $3} END { print sum }' ./file.txt" => awk program에서 변수의 사용을 통해 특정 필드의 값을 더하고, 더해진 총 합을 출력할 수 있다. 이 때, 총합은 모든 레코드 탐색이 끝난 시점인, "END" 패턴의 액션에서 실행
  -> "awk '{ for (i=2; i<=NF; i++) total += $i }; END { print "TOTAL : "total }' ./file.txt" => for 루프를 수행하여 여러 필드의 값을 연산에 포함시킬 수 있다. 참고로 아래 예제에서 "NF"는 현재 레코드의 필드 갯수를 뜻하며, "$i"는 변수 i가 매핑된 필드를 뜻한다.
  -> "awk '{ sum = 0 } {sum += ($3+$4+$5) } { print $0, sum, sum/3 }' ./file.txt" => 변수 및 액션을 조합하여 레코드 단위로 필드들의 값 및 평균을 계산하여 출력할 수 있다.
  -> "awk '{print $1, $2, $3+2, $4, $5}' ./file.txt" => awk program 표현식을 사용하여, 필드에 연산을 수행한 결과를 출력할 수 있다.
  -> "awk ' length($2) > 4 { print $0 } ' ./file.txt " => length() 함수를 사용해 레코드 또는 필드의 문자열 길이를 확인할 수 있다.
  -> "awk -f awkp.script ./file.txt " => awk 실행 시, "-f" 옵션을 사용하여 파일에 저장된 awk program을 실행할 수 있다.
  -> "awk -F ',' '{ print $1 }' ./file.txt" => 기본적으로 레코드의 필드를 구분하는 문자는 space 이다. 이를 "-F" 사용하여 구분문자를 변경할 수 있다.
  -> "awk '{ print $0 }' file.txt | sort (오름차순)" => awk 명령과 sort 명령을 조합하여, awk 실행 결과로 출력되는 레코드를 정렬할 수 있다.
  -> "awk '{ print $0; exit }' file.txt (첫 번째 레코드만 출력하고 실행 중지) => exit 키워드를 사용하여 특정 레코드만 출력 후 awk실행을 중지할 수 있습니다. 
  -> "awk '{ printf "%-3s %-8s %-4s %-4s %-4s\n", $1, $2, $3, $4, $5}' file.txt" => printf 함수를 사용하여 필드 값 출력 포맷을 지정하여 출력 너비를 지정할 수 있습니다.
  -> "awk '{max = 0; for (i=3; i<NF; i++) max = ($i > max) ? $i : max ; print max}' ./file.txt" 코드를 통해 레코드 내 필드의 최대 값을 구하여 출력할 수 있다.
  
  -> awk program 이 프로그래밍 언어로 작성되는 만큼 다양한 요소들을 사용하여 프로그래밍됩니다. 먼저 awk 표현식은 C 프로그래밍 언어 표현식과 유사한 형태로 제공된다. 
  -> awk program 키워드
     BEGIN   delete  END     function    in      printf
    break   do      exit    getline     next    return
    continue        else    for         if      print      while
    
  -> awk program 에서는 새로운 변수를 선언하고 값을 할당하거나 참조할 수 있습니다. 그리고 아래와 같이 특수 목적으로 미리 정의된 변수들을 사용할 수 있다.
    ARGC        : ARGV 배열 요소의 갯수.
    ARGV        : command line argument에 대한 배열.
    CONVFMT     : 문자열을 숫자로 변경할 때 사용할 형식. (ex, "%.6g")
    ENVIRON     : 환경변수에 대한 배열.
    FILENAME    : 경로를 포함한 입력 파일 이름.
    FNR         : 현재 파일에서 현재 레코드의 순서 값.
    FS          : 필드 구분 문자. (기본 값 = space)
    NF          : 현재 레코드에 있는 필드의 갯수.
    NR          : 입력 시작 점에서 현재 레코드의 순서 값.
    OFMT        : 문자열을 출력할 때 사용할 형식.
    OFS         : 결과 출력 시 필드 구분 문자. (기본 값 = space)
    ORS         : 결과 출력 시 레코드 구분 문자. (기본 값 = newline)
    RLENGTH     : match 함수에 의해 매칭된 문자열의 길이.
    RS          : 레코드 구분 문자. (기본 값 = newline)
    RSTART      : match 함수에 의해 매칭된 문자열의 시작 위치.
