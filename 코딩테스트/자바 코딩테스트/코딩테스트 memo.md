---
title: "코딩테스트 memo"
date: 
category: "코딩테스트"
tags: [변수, 코딩테스트, 함수형프로그래밍]
---

# 코딩테스트 memo

> 내적연산, 외적연산?!?!?!

---

벡터
내적연산, 외적연산?!?!?!


자바에서 람다식(lambda expression)은 함수형 프로그래밍을 지원하기 위한 기능 중 하나입니다. 기존의 자바에서는 메소드를 호출하기 위해 객체를 생성하고, 그 객체를 이용해 메소드를 호출하는 방식으로 처리되었습니다. 하지만 람다식을 이용하면 함수를 변수처럼 다룰 수 있습니다.

람다식은 다음과 같은 구조를 가집니다.

```java
(parameter) -> { body }
// 여기서 parameter는 매개변수를 나타내고, body는 람다식의 구현부분입니다.

// 예를 들어, 다음은 람다식을 이용해 add 메소드를 정의하는 예제입니다.

interface Addable {
    int add(int x, int y);
}

public class Main {
    public static void main(String[] args) {
        Addable add = (x, y) -> x + y;
        System.out.println(add.add(10, 20)); // 30
    }
}
위 예제에서 Addable은 함수형 인터페이스입니다. add 메소드는 두 개의 정수를 매개변수로 받아서, 그 합을 반환합니다. add 변수는 람다식으로 구현된 함수를 참조합니다. 람다식에서는 add 메소드의 구현부분이 {} 안에 작성됩니다.

람다식을 이용하면 코드가 간결해지고, 가독성이 좋아집니다. 또한, 람다식을 이용하면 함수형 인터페이스를 구현하는 클래스나 익명 클래스를 작성하지 않아도 되므로, 코드의 양이 줄어들고 유지보수가 쉬워집니다.

public static boolean isPrime(int n) {
    if (n < 2) {
        return false;
    }
    boolean[] isPrime = new boolean[n + 1];
    Arrays.fill(isPrime, true);

    for (int i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (int j = i * i; j <= n; j += i) {
                isPrime[j] = false;
            }
        }
    }
    return isPrime[n];
}
Java의 :: 연산자는 메서드 레퍼런스(Method Reference)를 생성하는 데 사용됩니다. 메서드 레퍼런스는 람다 표현식(lambda expression)과 유사한 기능을 제공하지만, 기존에 정의된 메서드를 참조하므로 코드의 가독성을 높이고 중복 코드를 줄이는 데에 도움을 줍니다.

메서드 레퍼런스는 :: 연산자를 사용하여 생성됩니다. 다음은 :: 연산자를 사용하여 정적 메서드 레퍼런스와 인스턴스 메서드 레퍼런스를 생성하는 예시입니다.

// 정적 메서드 레퍼런스 생성 예시
Function<String, Integer> parseIntFunction = Integer::parseInt;

// 인스턴스 메서드 레퍼런스 생성 예시
String str = "Hello World";
Consumer<String> printConsumer = System.out::println;
위의 예시에서 Integer::parseInt는 Integer 클래스의 정적 메서드인 parseInt를 참조하며, System.out::println은 System.out 객체의 인스턴스 메서드인 println을 참조합니다.

메서드 레퍼런스는 람다 표현식과 마찬가지로 함수형 인터페이스(functional interface)를 구현하는 데 사용될 수 있습니다. 예를 들어, Function<String, Integer> 인터페이스는 String 타입의 입력값을 받아서 Integer 타입의 결과값을 반환하는 함수형 인터페이스입니다. 따라서 위의 예시에서 parseIntFunction 변수는 String 타입의 입력값을 받아서 Integer 타입의 결과값을 반환하는 함수를 참조하게 됩니다.

Java 8부터 추가된 메서드 레퍼런스 기능은 코드를 더욱 간결하고 가독성 높은 코드로 변환하는 데에 큰 도움을 줍니다.

개선된 for 문
 
조건
1.JDK 1.5 이상
2.사용할 변수는 지역변수로 인식된다. (For문 안에서 사용되기 때문)
3. 대상은 배열 or 여러 원소를 포함한 자료형이어야 한다.

장점
1.간편한,가독성 좋은 코드
2. 배열 인덱스 문제 해결 (ArrayIndexOutOfBoundsException 예외를 피할 수 있다.)

단점
1.인덱스를 사용하지 못한다.(일반 for문의 (int i=0;) 할 때 i 같은 인덱스를 말하는 것) 하지만 방법이 있다.
★ 중요 ★
2.배열이나 ArrayList 값을 사용할 순 있지만 절대 수정할 수는 없다.

자주 사용되는 상황
1.ArrayList 원소 출력
2.배열 원소 출력
문법
for(자료형 변수명 : 배열명){
	문장
}
쉽게 설명하면
for(자료형 한 단계 아래의 자료형의 변수명 : 배열명){
}
정확히 말하면 아래의 자료형이 아니지만 이렇게 생각하면 이해가 쉽더라고요.
실전 예제 - 일반 배열 원소 추출
String[] arr = {"1-1","1-2","1-3","1-4","1-5"};
for(String s : arr) {
 System.out.println(s);
}
//결과 -> 1-1, 1-2, 1-3, 1-4, 1-5
