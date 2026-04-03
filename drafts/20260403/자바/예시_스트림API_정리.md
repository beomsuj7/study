---
title: "예시 - Java Stream API 정리"
date: 2026-04-03
category: "자바"
tags: [Java, Stream, 함수형프로그래밍]
---

# Java Stream API 정리

> Java 8 이후 도입된 Stream API의 핵심 개념과 사용법 정리

---

## Stream이란?

데이터 컬렉션을 **선언적으로** 처리할 수 있게 해주는 API이다.
반복문 대신 파이프라인 형태로 데이터를 변환/필터링/집계할 수 있다.

### 특징

- **지연 연산** (Lazy Evaluation): 최종 연산이 호출될 때까지 중간 연산은 실행되지 않음
- **일회용**: 한 번 사용하면 재사용 불가
- **원본 데이터 변경 없음**: 원본 컬렉션을 수정하지 않음

---

## 주요 메서드

### 중간 연산 (Intermediate Operations)

```java
// filter - 조건에 맞는 요소만 추출
List<String> result = names.stream()
    .filter(name -> name.startsWith("김"))
    .collect(Collectors.toList());

// map - 요소를 변환
List<Integer> lengths = names.stream()
    .map(String::length)
    .collect(Collectors.toList());

// sorted - 정렬
List<String> sorted = names.stream()
    .sorted()
    .collect(Collectors.toList());
```

### 최종 연산 (Terminal Operations)

```java
// collect - 결과를 컬렉션으로 수집
List<String> list = stream.collect(Collectors.toList());

// forEach - 각 요소에 작업 수행
names.stream().forEach(System.out::println);

// reduce - 모든 요소를 하나로 합침
int sum = numbers.stream().reduce(0, Integer::sum);
```

---

## 핵심 정리

1. Stream은 **선언적 데이터 처리** 도구다
2. 중간 연산은 **지연 실행**되고, 최종 연산이 트리거한다
3. `collect()`, `forEach()`, `reduce()`가 대표적인 최종 연산이다

---

## 참고 자료

- [Oracle - Stream API 공식 문서](https://docs.oracle.com/javase/8/docs/api/java/util/stream/Stream.html)
