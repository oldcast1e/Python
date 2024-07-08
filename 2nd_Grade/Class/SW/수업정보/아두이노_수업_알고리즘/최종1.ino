#include <ThreeWire.h>               // RTC 모듈 사용을 위한 라이브러리
#include <RtcDS1302.h>               // RTC 모듈 사용을 위한 라이브러리
#include <Adafruit_GFX.h>            // TFT 디스플레이 사용을 위한 라이브러리
#include <MCUFRIEND_kbv.h>           // TFT 디스플레이 사용을 위한 라이브러리
#include <DHT.h>                     // DHT 센서 사용을 위한 라이브러리

#define DHTPIN 41                    // DHT 센서의 데이터 핀
#define DHTTYPE DHT11                // DHT 센서 유형

const int soundSensorPin = A13;      // 고감도 사운드 센서 핀
const int buzzerPin = 51;            // 능동 부저 센서 핀
const int threshold = 80;            // 사운드 센서 값의 임계값 설정

DHT dht(DHTPIN, DHTTYPE);            // DHT 센서 객체 생성
ThreeWire myWire(32, 31, 35);        // DAT, CLK, RST 디지털 연결 번호
RtcDS1302<ThreeWire> Rtc(myWire);    // RTC 모듈 객체 생성

MCUFRIEND_kbv tft;                   // TFT 디스플레이 객체 생성

unsigned long previousMillis = 0;    // 이전 시간 저장 변수
bool displayedSejong = false;        // "Sejong University" 출력 여부를 추적하기 위한 변수
unsigned long sejongDisplayStart = 0;// "Sejong University" 출력 시작 시간

typedef struct sejongclass {         // 수업 정보를 저장하는 구조체
    char class_name[40];
    float class_start_c_time;
    float class_end_c_time;
    struct sejongclass* next;
} sejongclass;

typedef struct days {                // 하루의 수업 정보를 저장하는 구조체
    sejongclass* H;
} days;

int isEmpty(struct days* L) {        // 리스트가 비어있는지 확인하는 함수
    return L->H == NULL;
}

void schedule(struct days* L, const char* name, float st, float et) { // 수업 정보를 리스트에 추가하는 함수
    sejongclass* node = (sejongclass*)malloc(sizeof(sejongclass));
    if (node == NULL) {
        Serial.println("Memory allocation failed");
        return;
    }

    strcpy(node->class_name, name);
    node->class_start_c_time = st;
    node->class_end_c_time = et;
    node->next = NULL;

    if (isEmpty(L)) {
        L->H = node;
    } else {
        sejongclass* p;
        for (p = L->H; p->next != NULL; p = p->next);
        p->next = node;
    }
}

void class_check(days* L, float c_time, int year, int month, int dayOfMonth, int hour, int minute) { // 현재 시간과 수업 시간을 비교하여 디스플레이에 출력하는 함수
    sejongclass* p;
    int flag = 0;
    tft.fillScreen(TFT_WHITE);  // 화면 초기화
    tft.setTextColor(TFT_BLACK);
    tft.setTextSize(3);

    // RTC 모듈의 출력
    tft.setCursor(10, 5);  // 초기 커서 위치 설정
    tft.print(year);
    tft.print("-");
    if (month < 10) tft.print("0");
    tft.print(month);
    tft.print("-");
    if (dayOfMonth < 10) tft.print("0");
    tft.print(dayOfMonth);
    tft.print(" ");
    if (hour < 10) tft.print("0");
    tft.print(hour);
    tft.print(":");
    if (minute < 10) tft.print("0");
    tft.println(minute);

    for (p = L->H; p != NULL; p = p->next) {
        if (c_time >= p->class_start_c_time && c_time <= p->class_end_c_time) {
            flag = 1;

            char* c_name = p->class_name;
            int starthour = (int)p->class_start_c_time, endhour = (int)p->class_end_c_time;
            int startmin = (p->class_start_c_time - starthour) * 60;
            int endmin = (p->class_end_c_time - endhour) * 60;
            tft.setTextSize(3);
            tft.setCursor(10, 105);

            // 수업 정보 출력
            Serial.print(c_name);
            Serial.print(' ');
            Serial.print(starthour);
            Serial.print(':');
            if (startmin < 10) Serial.print('0');
            Serial.print(startmin);
            Serial.print('~');
            Serial.print(endhour);
            Serial.print(':');
            if (endmin < 10) Serial.print('0');
            Serial.println(endmin);

            tft.setCursor(10, 55);  // 초기 커서 위치 설정
            tft.setTextColor(TFT_BLUE);
            tft.print(c_name);
            tft.print(' ');
            tft.print(starthour);
            tft.print(':');
            if (startmin < 10) tft.print('0');
            tft.print(startmin);
            tft.print('~');
            tft.print(endhour);
            tft.print(':');
            if (endmin < 10) tft.print('0');
            tft.println(endmin);

            tft.setCursor(10, 105);  // 초기 커서 위치 설정
            tft.print("Attendance Info: ");
            if (c_time > p->class_start_c_time && c_time <= (p->class_start_c_time + 0.0833333)) {
                tft.setTextSize(3);
                tft.setTextColor(TFT_GREEN);
                tft.println("Attendance");
            } else if (c_time > p->class_start_c_time + 0.25 && c_time <= (p->class_end_c_time)) {
                tft.setTextSize(3);
                tft.setTextColor(TFT_RED);
                tft.println("Absent");
            } else if (c_time > p->class_start_c_time + 0.0833333 && c_time <= (p->class_start_c_time + 0.25)) {
                tft.setTextSize(3);
                tft.setTextColor(TFT_RED);
                tft.println("Late");
            }
        }
    }
    if (flag == 0) {
        Serial.println("수업이 없습니다.");
        tft.println("No schedule.");
    }
    tft.println(); // 줄바꿈 추가
}

int getWeekday(int year, int month, int dayOfMonth) { // 요일 계산 함수
    bool isLeapYear = (year % 4 == 0 && year % 100 != 0) || (year % 400 == 0);
    int daysInMonth[] = {31, 28 + isLeapYear, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    int days = dayOfMonth - 1;
    for (int i = 0; i < month - 1; ++i) {
        days += daysInMonth[i];
    }
    for (int i = 1; i < year; ++i) {
        days += (i % 4 == 0 && i % 100 != 0) || (i % 400 == 0) ? 366 : 365;
    }
    return (days + 2) % 7; // 2024년 1월 1일은 화요일이므로, 0: 화요일, 1: 수요일, ..., 6: 월요일
}

const char* getWeekdayString(int weekday) { // 요일 문자열 반환 함수
    switch (weekday) {
        case 0: return "Sun";
        case 1: return "Mon";
        case 2: return "Tue";
        case 3: return "Wed";
        case 4: return "Thu";
        case 5: return "Fri";
        case 6: return "Sat";
        default: return ""; // 예외 처리
    }
}

void check(const char* day, int year, int month, int dayOfMonth, int hour, int minute, int second) { // 요일에 따른 수업 정보를 설정하는 함수
    days d;
    d.H = NULL;

    if (strcmp(day, "Mon") == 0) {
        schedule(&d, "Creative SW", 9.0, 12.0);
        schedule(&d, "Creative SW", 12.0, 15.0);
        schedule(&d, "Probability and Statistics", 16.5, 18.0);
    } else if (strcmp(day, "Tue") == 0) {
        schedule(&d, "Creative SW", 9.0, 12.0);
        schedule(&d, "Electric Circuits", 12.0, 13.5);
        schedule(&d, "Probability and Statistics", 13.5, 15.0);
        schedule(&d, "Telecommunication Systems", 15.0, 16.5);
        schedule(&d, "Linear Algebra and Programming", 18.0, 21.0);
    } else if (strcmp(day, "Wed") == 0) {
        schedule(&d, "Unmanned Vehicle Integration Project (Graduate Course)", 9.0, 12.0);
        schedule(&d, "Doctoral Dissertation Research(Graduate Course)", 12.0, 13.5);
        schedule(&d, "Career conference", 13.5, 15.0);
        schedule(&d, "Probability and Statistics", 16.5, 18.0);
        schedule(&d, "Linear Algebra and Programming", 19.5, 21.0);
    } else if (strcmp(day, "Thu") == 0) {
        schedule(&d, "Creative SW", 9.0, 12.0);
        schedule(&d, "Electric Circuits", 12.0, 13.5);
        schedule(&d, "Probability and Statistics", 13.5, 15.0);
        schedule(&d, "Telecommunication Systems", 15.0, 16.5);
        schedule(&d, "AI Robot Design", 16.5, 19.5);
    } else {
        schedule(&d, "Semiconductor Device", 9.0, 12.0);
        schedule(&d, "Doctoral Dissertation Research(Graduate Course)", 12.0, 13.5);
        schedule(&d, "CapstonDesign(Industry-Academia Collaboration Project)", 13.5, 19.5);
        schedule(&d, "Linear Algebra and Programming", 19.5, 21.0);
    }

    float c_time = hour + minute / 60.0 + second / 3600.0;
    class_check(&d, c_time, year, month, dayOfMonth, hour, minute);

    sejongclass* curr = d.H;
    while (curr != NULL) {
        sejongclass* next = curr->next;
        free(curr);
        curr = next;
    }
}

void setup() {
    Serial.begin(9600);              // 시리얼 통신 시작
    Rtc.Begin();                     // RTC 모듈 시작
    RtcDateTime compiled = RtcDateTime(__DATE__, __TIME__); // 현재 시간 설정
    Rtc.SetDateTime(compiled);       // RTC 시간 설정

    pinMode(buzzerPin, OUTPUT);      // 부저 핀을 출력 모드로 설정

    uint16_t ID = tft.readID();      // TFT 디스플레이 ID 읽기
    tft.begin(ID);                   // TFT 디스플레이 시작
    tft.setRotation(1);              // 디스플레이 회전 설정
    tft.fillScreen(TFT_WHITE);       // 화면 초기화

    dht.begin();                     // DHT 센서 시작
}

void loop() {
    unsigned long currentMillis = millis(); // 현재 시간 읽기

    int soundLevel = analogRead(soundSensorPin); // 사운드 센서 값 읽기
    Serial.print("soundLevel : ");
    Serial.println(soundLevel);

    // 10초마다 실행
    if (currentMillis - previousMillis >= 10000) {
        previousMillis = currentMillis;

        RtcDateTime now = Rtc.GetDateTime(); // 현재 시간 읽기
        int year = now.Year(), month = now.Month(), dayOfMonth = now.Day(), hour = now.Hour(), minute = now.Minute(), second = now.Second();
        int weekday = getWeekday(year, month, dayOfMonth);
        const char* weekdayString = getWeekdayString(weekday);

        // 온습도 값 읽기
        float humidity = dht.readHumidity();
        float temperature = dht.readTemperature();

        // 정각 확인
        if (minute == 0 && !displayedSejong) {
            tft.fillScreen(TFT_WHITE);
            tft.setTextColor(TFT_BLACK);
            tft.setTextSize(3);
            tft.setCursor(10, 50);
            tft.println("Sejong University");
            displayedSejong = true; // 정각 메시지 출력 후 플래그 설정
            sejongDisplayStart = currentMillis; // 출력 시작 시간 저장
        }

        // 5초간 "Sejong University"를 출력 후 원래 화면으로 복귀
        if (displayedSejong && (currentMillis - sejongDisplayStart >= 5000)) {
            displayedSejong = false; // 플래그 초기화
            check(weekdayString, year, month, dayOfMonth, hour, minute, second); // 원래 화면으로 복귀
        }

        // 정각이 아니면 원래 화면 유지
        if (!displayedSejong) {
            check(weekdayString, year, month, dayOfMonth, hour, minute, second);

            // 온습도 정보 출력
            tft.setCursor(10, 155);
            tft.setTextSize(3);
            tft.setTextColor(TFT_BLACK);
            tft.print("Tmp: ");
            tft.print(temperature);
            tft.println(" C   ");
            tft.setCursor(10, 180);
            tft.print("Hum: ");
            tft.print(humidity);
            tft.print(" %");

            // 사운드 레벨 체크 및 부저/메시지 출력
            if (soundLevel > threshold) {
                digitalWrite(buzzerPin, HIGH); // 임계값을 초과하면 부저를 켬
                tft.setTextSize(3);
                tft.setTextColor(TFT_RED); // 경고 메시지 색상 변경
                tft.setCursor(10, 230);
                tft.print("Excess decibels");
            } else {
                digitalWrite(buzzerPin, LOW); // 임계값 이하일 때 부저 끔
                tft.setTextSize(3);
                tft.setTextColor(TFT_BLACK);
                tft.setCursor(10, 230);
                tft.print("Appropriate decibels");
            }
        }
    }
}
