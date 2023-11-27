package 그리디;

import java.util.Scanner;
import java.lang.Math;

public class P1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[][] meeting = new int[N][2]; // 0번째 열은 시작 시간, 1번째 열은 끝나는 시간
        int check = 0;
        int count = 0; // 회의의 갯수

        for (int i = 0; i < N; i++) { // 입력 받기 수행
            meeting[i][0] = sc.nextInt();
            meeting[i][1] = sc.nextInt();
        }

        int max = -2147000000;
        for (int i = 0; i < N; i++) { //가장 늦게 끝나는 회의 시간 설정
            max = Math.max(max, meeting[i][1]);
        }
        //회의실 배정
        // 1. check 시간 보다는 시작시간이 크고, 끝나는 시간이 가장 빠른 친구

        do {
            int fastest = max;
            int i;
            for (i = 0; i < N; i++) { // 배열을 돌면서 시작시간이 체크시간보다 느린 회의 시간은 제외
                if ((meeting[i][0] >= check) && (meeting[i][1] <= fastest)) { // 시작 시간이 check 시간보다 늦은경우만 실행
                    fastest = meeting[i][1];
                }
            }
            check = fastest;
            count++;
            if(fastest==max){break;}
        } while (true);
        System.out.println(count);
    }
}

