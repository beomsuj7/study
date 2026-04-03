---
title: "ECMAscript"
date: 2023-01-12
category: "KOSA수업"
tags: [JavaScript, KOSA]
---

# ECMAscript

> Javascript를 표준화하기 위해 만들어졌다.

---

Javascript를 표준화하기 위해 만들어졌다.
Ecma International이 ECMA-262 기술 규격에 따라 정의하고 있는 표준화된 스크립트 프로그래밍 언어를 말한다. ECMA스크립트는 웹의 클라이언트 사이드 스크립트로 많이 사용되며 Node.js를 사용한 서버 응용 프로그램 및 서비스에도 점차 많이 쓰이고 있다.
# Javascript
Front-end web application 부분에서 JavaScript가 사용된다.
객체 기반의 스크립트 프로그래밍 언어이다. 이 언어는 웹 브라우저 내에서 주로 사용되며, 다른 응용 프로그램의 내장 객체에도 접근할 수 있는 기능을 가지고 있다. 또한 Node.js와 같은 런타임 환경과 같이 서버 프로그래밍에도 사용되고 있다. 
### 역사 (중요X)
1993년, 일리노이 대학교 어배너-섐페인의 NCSA는 최초의 대중적인 그래픽 웹 브라우저인 NCSA 모자이크를 출시하였다. 1994년, 모자이크 커뮤니케이션스라는 이름의 회사가 캘래포니아주 마운틴 뷰에 설립되었으며 모자이크 넷스케이프를 만들기 위해 오리지널 NCSA 모자이크 개발자들을 고용하였다. 넷스케이프 커뮤니케이션스는 넷스케이프 내비게이터 썬의 더 정적인 프로그래밍 언어인 자바를 포함시키기 위해 썬 마이크로시스템즈와 협업하였다. 넷스케이프 커뮤니케이션스는 이때 자신들이 만들기 바랐던 스크립트 언어가 자바를 구현할 것이고 비슷한 문법을 채용하는 것이 좋겠다고 생각했으며 펄, 파이썬, Tcl, 스킴 등 기타 언어를 채택하는 것을 배제하였다. 
### 자바와 자바스크립트(표준화이름 = ECMAScript)
자바스크립트라는 이름은 상당한 혼란을 가져왔다. 이것은 자바와 자바스크립트 간에는 구문이 유사하다는 점(양쪽 모두 C에 바탕을 두었기 때문에) 외에는 실제 관련성이 없었기 때문이다. 두 언어는 의미론적으로 매우 다르고, 특히 각각의 객체 모델은 관련성이 없는 데다가 상당 부분이 호환되지 않는다.
### JavaScript 구성
- ECMAScrpt(core language)
- api 1. client-side web 2. HostAPI

## Fragmentation(파편화현상)
ECMA표준 -> ECMAScrpt
(browser API) 구현은 당연히 각 Vendor들이한다.
JavaScript (Frontend)가 가장 갖고있는 문제점중 하나가 모든 브라우져에서 안돌아가는(파편화현상)을 갖고있다.

### 자주사용하는 5대 브라우져
                    Javascript Engine
Chrome              V8
IE -> Edge          Chakra
Safari              Webkit
FireFoxs            spiderMonkey
Opera
표준을 가장 잘지키는 브라우져는 Chrome이다. 
Default Browser -> Chrome (V8 engine) 사용
### JavaScript 문제점
1. 언어의 모호성
2. 구현이 어렵다.
3. Fragmentation(파편화현상)
### JQuery
1. 구현에 용이
2. Fragment 해결
### (World Wide Web Consortium)W3c -> 기본적인 web표준을 관리하는 기구
HTML -> 문서의 내용, 구조   
CSS -> Styling
HTML의 Version을 올리지 않는다.(HTML 4.01)
1. 정형성이 없다 -> 유지보수성도 없다.
2. 확장성이 없다. <HTML//>, <title//>, 등등
-> XML 졍형화된 문법, 확정성이 있다.   
-> XHTML 새로운 표준안 

WHATWQ
-> Web Hypertent
-> Application Technology
-> Working Group
## ★ HTML5 ★
XML을 이용하지 않고 web application을 만들 수 있도록 HTML을 발전시키자
HTML(기능추가)
CSS(기능추가)
JavaScript (70% 이상)

HTML5라고 불리는 개념은 단순히 웹 문서를 작성할 때 사용되는 마크업 랭귀지(HTML)의 문법적(syntactic) 버전뿐만 아니라 새로운 DOM API 스펙을 포함하는 것이다.
문법면에서는 이전에 비해 상당히 간결하고 명확해졌다. XML 문법도 모두 제거되어 이전에는 JavaScript를 사용해서 엄청나게 긴 코드를 써서 간접적으로 구현해야 했던 기능들이 정식 엘리먼트로 편입됨으로써 간단하게 구현해낼 수 있게 되었고, 불필요하게 길게 적어야 했던 이전 버전에서 꼭 필요한 부분만 남기도록 바뀌는 등 여러가지 개선점이 생겼다.
이런 API들은 사실상의 브라우저 표준 스크립트 언어인 JavaScript를 통해 이용할 수 있다. 이때문에 HTML5는 마크업 언어라고만 보기는 더 이상 힘들어졌다. HTML5 그 자체가 제공하는 것은 문서 구조와 API이고, 이걸 API와 연결시켜 실제 동작을 구현하는 것은 JavaScript라는 언어로, 이 둘은 엄연히 별개의 것이다. HTML5와 JavaScript가 서로 연결되어 돌아가는 개념이지, HTML5 안에 JavaScript가 포함되는 것이 절대로 아니다. 단적으로, JavaScript는 ECMAScript라는 표준안이 따로 나오는 별도의 프로그래밍 언어이다.
### Node.js
Back-end application을 JavaScript로 만들수 있게 만든다.

### Platform
다른 program을 실행시켜줄수 있는 Program

### Tool
Visual Studio code 프로그램(무료) -> 사용자가 많다.   
Web Storm (유료)
ex)
1. HTML 문서를 만들어야 한다.
2. JavaScript file을 HTML내에서 링크 건다.
3. Web Server Program이 있어야 한다. (live server 설치)
4. web의 기본적인 동작방식을 이해해 보자.
```Javascript
index.js
// 자바스크립트는 ArrayList가 없다.

// JavaScript의 기본 자료구조는 Array(배열)이다.
const myArray = [1, 2, 3, 4]
// 기본 for구문대신에 forEach를 이용.
myArray.forEach(function(data) {
    console.log(`결과는 : ` + data)
})
// 경고창을 띄워요!
// alert()는 browser가 가지고 있는 API
alert('소리없는 아우성')
// 실행되지 않는다
// ReferenceError: alert is not defined
test.html
<!-- !tap 사용시 자동으로 완성  -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="./index.js">
        // 경고창을 띄운다. alert()는 browser가 가지고 있는 api다.
        // alert('소리없는 아우성!') 이렇게 써도 되지만 하지 않는다.
    </script>
</head>
<body>
    소리없는 아우성!!!
</body>
</html>
<!-- !tap 사용시 자동으로 완성  -->
```
### alert(); browser API
(WEb API)
이기 떄문에 browser를 통해서 실행해야 한다.
HTML 안에 Javascript 포함시켜서 browser에서 실행한다.
// 경고창 alert()는 browser가 가지고 있는 API
// alert('소리없는 아우성')  -> 실행되지 않는다 ReferenceError: alert is not defined
// 서버 연결 이후부터 실행되기 때문에 alert에서 멈춰서 block 상태가 된다.
### Web -> c/s구조
Server computer, client computer
web server
-> 우리 프로젝트를 인식, web에 deploy 한다.
web client -> server computer 에게 HTTP 전송 -> client computer 에서 response(응답) 받음.
1. HTML 분석 -> DOM(Document Object Model)
2. CSS 분석 -> CSSOM
3. JavaScript 실행
4. Render Tree 화면에 그린다.
### 작성한 JavaScript code
실행하는 방법 2가지
1. Node JS 이용 (Code Runner)
2. Web Server를 이용(live Server)

## ECMAScript 2015 (ES6) 프로그래밍 언어 spec
ES3 -> ES5 -> ES6(ES2015) -> ES7(ES2016)
ECMAScript 2015 (ES6 또는 ES2015)
현재 ECMAScript 2016 (ES7)까지 버전이 나와 있기는 하지만 현재 시점에서 대부분 개발은 ECMAScript 2015버전을 많이 사용합니다.

computer는 CPU를 이용하여 연산 수행, 사용하는 데이터는 memory에 올라가 있어야한다.
Memory는 데이터를 저장할 수 있는 memorycell의 집합체(1byte)
### Declarlation - Variable(변수)
메모리 공간에 이름을 붙이는 Mechanism
idetntifier(식별자)   
프로그래머

변수의 선언 (Variable declaration)
JavaScript에서는 
Var, let, const
3가지중 한개를 이용하면 된다.
기존에는 var만 있었는데 es6들어오면서 const와 let가 추가되었다.
var - function level scope
const, let - block level scope
const - 자바의 finally랑 비슷하다

함수 레벨 스코프(Function-level scope) - var
함수 내에서 선언된 변수는 함수 내에서만 유효하며 함수 외부에서는 참조할 수 없다. 함수 내부에서 선언한 변수는 지역 변수이며 함수 외부에서 선언한 변수는 모두 전역 변수이다.

블록 레벨 스코프(Block-level scope) - const, let
모든 코드 블록내에서 선언된 변수는 코드 블록 내에서만 유효하며 코드 블록 외부에서는 참조할 수 없다. 즉, 코드 블록 내부에서 선언한 변수는 지역 변수이다.
result -> undefined(문자열이 아니라 java의 0과 같은 초기화)

### 호이스팅(Hoisting)의 개념
자바스크립트 함수는 실행되기 전에 함수 안에 필요한 변수값들을 모두 모아서 유효 범위의 최상단에 선언한다.
자바스크립트 Parser가 함수 실행 전 해당 함수를 한 번 훑는다.
함수 안에 존재하는 변수/함수선언에 대한 정보를 기억하고 있다가 실행시킨다.
유효 범위: 함수 블록 {} 안에서 유효
즉, 함수 내에서 아래쪽에 존재하는 내용 중 필요한 값들을 끌어올리는 것이다.
실제로 코드가 끌어올려지는 건 아니며, 자바스크립트 Parser 내부적으로 끌어올려서 처리하는 것으로 실제 메모리에서는 변화가 없다.
var 변수 선언과 함수선언문에서만 호이스팅이 일어난다.
var 변수/함수의 선언만 위로 끌어 올려지며, 할당은 끌어 올려지지 않는다.
자바스크립트의 primitive type의 값은 다 immutable의 속성이 있다.
```javascript
// 변수를 선언
// console.log(result);
// var result = 100;
// 에러가 안뜬다.
// Hoisting 때문에 -> JavaScript의 실행은 2개의 Phase로 실행된다. 
// 1번쨰 Creating Phase -> 2번쨰 Excution Phase라고 한다.
// 모든 선언구문을 찾아서 식별자를 메모리에 매핑(변수화시키고) 끝나면 다시 돌아가서 코드를 실행한다.

// VAR keywrod는 같은 scope내에서 중복선언이 가능하다.
// var x = 100;
// var y = 200;

// var x = 300;  // var가 없는걸로 간주된다.
// x = 300;
// var y; // 이런경우는 무시

// var keyword는 function level scope만을 local scope로 인정한다.
// var x = 1;

// if (true) {
//     var x = 100;
// }
// console.log(x); // 100 function level scope라서
///////////////////////////////////////////////////
// Java는 함수가 없고 대신 method가 있다. method 는 class안에 위치한다. 
// JavaScript는 함수형 언어라서 함수가 존재한다. 
// 독립적으로 존재하기 때문에 함수를 만들떄는 function keyword를 사용한다.
// 당연히 함수이름이 있어야 하니 식별자를 붙여준다. 인자와 실행코드가 block으로 표현
// var x = 1;

// function myFunc() {
//     var x = 200;
//     console.log(x); // 1
// }

// console.log(x); // 1
// myFunc();
// console.log(x); // 200
// 출력 1 - 200 - 1
```
### Temporal Dead Zone (TDZ)
- 선언 단계(Declaration phase)
변수를 실행 컨텍스트의 변수 객체에 등록하는 단계를 의미합니다. 이 변수 객체는 스코프가 참조하는 대상이 됩니다.
- 초기화 단계(Initialization phase)
실행 컨텍스트에 존재 하는 변수 객체에 선언 단계의 변수를 위한 메모리를 만드는 단계 입니다. 이 단계에서 할당된 메모리에는 undefined로 초기화 됩니다.
- 할당 단계(Assignment phase)
사용자가 undefined로 초기화된 메모리의 다른 값을 할당하는 단계 입니다. 

- var 변수의 라이프사이클
var 키워드 변수는 변수 선언전에 선언 단계와 초기화 단계를 동시에 진행합니다.
그래서 javascript는 실행 컨텍스트 변수 객체의 변수를 등록하고 메모리를 undefined로 만들어 버립니다.
그렇기 때문에 변수를 선언하기 전에 호출을 해도 undefined로 호출이 되는 호이스팅이 발생하는 것 입니다.

- let의 라이프 사이클
let으로 선언된 변수는 var 키워드와는 다르게 선언단계와 초기화 단계가 분리되어서 진행이 됩니다.
그렇기 때문에 실행 컨텍스트에 변수를 등록했지만, 메모리가 할당이 되질 않아 접근할 수 없어 참조 에러(ReferenceError)가 발생하는 것입니다.
즉, let 또한 선언전, 실행 컨텍스트 변수 객체에 등록이 되어 호이스팅이 되지만,
이 TDZ 구간에 의해 메모리가 할당이 되질 않아 참조 에러(ReferenceError) 발생하는 것 입니다.
ex2)
```javascript
// 이번에는 let ES6에서 도입되었고 block level scope이고 알고 있는 변수방식을 이용한다.
// 같은 scope내에서 중복선언이 안된다.
// let result = 100;
// let result = 50;

// block level scope
// let score = 50;
// {let score = 100;
//  let myVar = 10;
// }
// console.log(score); // 50
// console.log(myVar); // Error

//////////////////////////////////
// let i = 100; // i는 전역변수(global variable)
// function myFunc() {
//     let i = 10; // i는 지역변수(local variable)

//     for (let i = 0; i<3; i++) {
//         console.log(i); // 0 1 2
//         process
//     }
// }
// myFunc();
// console.log(i); // 100

// console.log(x);  //undefined가 출력 안되고 error가 출력된다.
// let을 선언된 경우에는 hoisting 은 일어나지만 x를 사용할수 있게되는 시점은 x를 초기화한 이후부터 사용할 수 있다.
// 이 영역을 Temporal Dead Zone(TDZ) 라고 부른다.
// let x = 100;

// hosting은 var, let, const 전부 일어난다.
// let myVar = 1; // 전역변수(global variable) 
// {
//     console.log(myVar);
//     let myVar = 100; // hoisting 되기 때문에 그다음 TDZ가 생겨서 오류가 뜬다
// }
// console.log(myVar);

### 01_12 자바 스크립트 배운 내용 정리
1. Variable (변수)
2. 선언을 통해 변수를 생성 -> Javascript는 변수를 생성할떄 Data type을 명시하지 않는다 -> 만들어진 변수에 어떤 값이든 다 들어간다. (Weak Type)
3. 변수이름 -> 변수 식별자
4. var, let 차이점
5. Hoisting
6. JavaScript code Page
7. VAR -> 같은 scope 내에서 중복 선언 간으
8. let 같은 scope 내에서 중복 선언이 안되요
9. Creation phase 에서 생성된 변수에는 undefined
