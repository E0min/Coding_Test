package 그리디;

import java.util.ArrayList;
import java.util.Scanner;
import java.lang.Math;

public class P_1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        ArrayList<Integer> meeting = new ArrayList<>(); // 0번째 열은 시작 시간, 1번째 열은 끝나는 시간
        int check = 0;
        int count = 0; // 회의의 갯수

        for (int i = 0; i < N; i++) { // 입력 받기 수행
            meeting[i][0] = sc.nextInt();
            meeting[i][1] = sc.nextInt();
        }



        System.out.println(count);
    }
}

