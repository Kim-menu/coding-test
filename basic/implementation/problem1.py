#include <iostream>

using namespace std;


class time {
private:
    int hour = 0;
    int minute = 0;
    int second = 0;
public:
    void lapsed(void);
    int getHour(void){return hour;};
    bool includeThree(void);
};

void time::lapsed(void) {
    if(second < 59) second++;
    else if(minute < 59) {
        second = 0;
        minute++;
    }
    else{
        second = 0;
        minute = 0;
        hour++;
    }
}

bool time::includeThree(void) {
    if (hour % 10 == 3) return true;
    if (minute / 10 == 3) return true;
    if (minute % 10 == 3) return true;
    if (second / 10 == 3) return true;
    if (second % 10 == 3) return true;
    return false;
}

int main(void) {
    int N;
    int caseCount = 0;
    cin >> N;
    time myTime;
    while(myTime.getHour() <= N) {
        if (myTime.includeThree()) caseCount++;
        myTime.lapsed();
    }
    cout << caseCount;
    return 0;
}
