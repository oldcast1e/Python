#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const int ledPin = 13; // LED 핀 설정
unsigned long previousMillis = 0; // 이전 시간 저장
const long interval = 60000; // 1분 간격으로 시간 출력하기

int year, month, day, hour, minute, second; // 시간 변수 선언

void setup() {
  Serial.begin(9600); // 시리얼 통신 시작
  pinMode(ledPin, OUTPUT); // LED 핀을 출력으로 설정

  // 초기 시간 입력 받기
  Serial.println("Enter the current date and time (YYYY/MM/DD HH:MM:SS):");
  while (!Serial.available()) {} // 사용자 입력이 있을 때까지 대기
  readTime(); // 시간 읽기 함수 호출
  Serial.println("Time set.");
}

void loop() {
  unsigned long currentMillis = millis(); // 현재 시간 가져오기
  
  if (currentMillis - previousMillis >= interval) { // 시간 간격이 지났는지 확인
    previousMillis = currentMillis; // 시간 업데이트
    updateMinute(); // 1분마다 시간 업데이트 함수 호출
    checkClass(); // 수업 정보 확인 함수 호출
  }
}


void readTime() {
  year = Serial.parseInt();
  while (Serial.read() != '/') {}
  month = Serial.parseInt();
  while (Serial.read() != '/') {}
  day = Serial.parseInt();
  while (Serial.read() != ' ') {}
  hour = Serial.parseInt();
  while (Serial.read() != ':') {}
  minute = Serial.parseInt();
  while (Serial.read() != ':') {}
  second = Serial.parseInt();
}

void updateMinute() {
  minute++; // 분 증가
  if (minute >= 60) { // 60분이 되면
    minute = 0; // 0분으로 초기화
    hour++; // 시 증가
    if (hour >= 24) { // 24시가 되면
      hour = 0; // 0시로 초기화
      day++; // 일 증가
      // 달마다 일수가 다를 수 있으므로 해당 달의 마지막 날을 체크하여 일을 증가시킴
      if (day > daysInMonth(year, month)) {
        day = 1; // 다음 달로 넘어가기 위해 일을 1로 설정
        month++; // 달 증가
        if (month > 12) { // 12월을 넘어가면
          month = 1; // 1월로 초기화
          year++; // 년도 증가
        }
      }
    }
  }
}

void printTime() {
  Serial.print("Current time: ");
  Serial.print(year);
  Serial.print("/");
  if (month < 10) Serial.print("0");
  Serial.print(month);
  Serial.print("/");
  if (day < 10) Serial.print("0");
  Serial.print(day);
  Serial.print(" ");
  if (hour < 10) Serial.print("0");
  Serial.print(hour);
  Serial.print(":");
  if (minute < 10) Serial.print("0");
  Serial.print(minute);
  Serial.print(":");
  if (second < 10) Serial.print("0");
  Serial.println(second);
}

void checkClass() {
  int dayOfWeek = getDayOfWeek(year, month, day); // 현재 요일 구하기
  float currentTime = hour + minute / 60.0; // 현재 시간대 구하기
  const char* days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

  Serial.print("Current time: ");
  Serial.print(year);
  Serial.print("/");
  Serial.print(month);
  Serial.print("/");
  Serial.print(day);
  Serial.print(" ");
  Serial.print(hour);
  Serial.print(":");
  Serial.print(minute);
  Serial.print(":");
  Serial.println(second);

  Serial.print("Day of the week: ");
  Serial.println(days[dayOfWeek]);

  // 요일과 현재 시간대에 해당하는 수업 정보 출력
  class_check(days[dayOfWeek], currentTime);
}


void printDay() {
  const char* days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
  int dayOfWeek = getDayOfWeek(year, month, day);
  Serial.print("Day of the week: ");
  Serial.println(days[dayOfWeek]);
}

void checkClass() {
  int dayOfWeek = getDayOfWeek(year, month, day); // 현재 요일 구하기
  float currentTime = hour + minute / 60.0; // 현재 시간대 구하기
  const char* days[] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};

  Serial.print("Current time: ");
  Serial.print(year);
  Serial.print("/");
  Serial.print(month);
  Serial.print("/");
  Serial.print(day);
  Serial.print(" ");
  Serial.print(hour);
  Serial.print(":");
  Serial.print(minute);
  Serial.print(":");
  Serial.println(second);

  Serial.print("Day of the week: ");
  Serial.println(days[dayOfWeek]);

  // 요일과 현재 시간대에 해당하는 수업 정보 출력
  if (strcmp(days[dayOfWeek], "Monday") == 0 && (currentTime >= 9.0 && currentTime <= 12.0 ||
                                                  currentTime >= 12.0 && currentTime <= 15.0 ||
                                                  currentTime >= 16.5 && currentTime <= 18.0)) {
    Serial.println("창의SW기초설계");
  } else if (strcmp(days[dayOfWeek], "Tuesday") == 0 && (currentTime >= 9.0 && currentTime <= 12.0 ||
                                                          currentTime >= 12.0 && currentTime <= 13.5 ||
                                                          currentTime >= 13.5 && currentTime <= 15.0 ||
                                                          currentTime >= 15.0 && currentTime <= 16.5 ||
                                                          currentTime >= 18.0 && currentTime <= 21.0)) {
    Serial.println("창의SW기초설계");
  } else if (strcmp(days[dayOfWeek], "Wednesday") == 0 && (currentTime >= 9.0 && currentTime <= 12.0 ||
                                                            currentTime >= 12.0 && currentTime <= 13.5 ||
                                                            currentTime >= 13.5 && currentTime <= 13.0 ||
                                                            currentTime >= 16.5 && currentTime <= 18.0 ||
                                                            currentTime >= 19.5 && currentTime <= 21.0)) {
    Serial.println("무인이동체융합프로젝트(대학원)");
  } else if (strcmp(days[dayOfWeek], "Thursday") == 0 && (currentTime >= 9.0 && currentTime <= 12.0 ||
                                                           currentTime >= 12.0 && currentTime <= 13.5 ||
                                                           currentTime >= 13.5 && currentTime <= 15.0 ||
                                                           currentTime >= 15.0 && currentTime <= 16.5 ||
                                                           currentTime >= 16.5 && currentTime <= 19.5)) {
    Serial.println("창의SW기초설계");
  } else if (strcmp(days[dayOfWeek], "Friday") == 0 && (currentTime >= 9.0 && currentTime <= 12.0 ||
                                                         currentTime >= 12.0 && currentTime <= 13.5 ||
                                                         currentTime >= 13.5 && currentTime <= 19.5 ||
                                                         currentTime >= 19.5 && currentTime <= 21.0)) {
    Serial.println("반도체소자");
  } else {
    Serial.println("수업이 없습니다");
  }
}




int daysInMonth(int year, int month) {
  int days[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
  if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
    days[1] = 29; // 윤년인 경우 2월의 일 수 변경
  }
  return days[month - 1]; // 인덱스는 0부터 시작하므로 1을 빼줌
}

int getDayOfWeek(int year, int month, int day) {
  int t = (14 - month) / 12;
  int y = year - t;
  int m = month + 12 * t - 2;
  int d = (day + y + y / 4 - y / 100 + y / 400 + (31 * m) / 12) % 7;
  return d;
}
