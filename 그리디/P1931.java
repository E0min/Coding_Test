package 그리디;
import java.util.Scanner;
import java.util.Collections;
import java.util.Arrays;

public class P1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int [][] meeting = new int[N][];
        int check = 0; // 회의실 마지막 사용 시간 체크
        int count = 0; // 회의의 갯수


        for (int i=0 ; i<=N ; i++){ // 입력 받기 수행
            meeting[N][0] = sc.nextInt();
            meeting[N][1] = sc.nextInt();
        }
        //회의실 배정
        // 1. check 시간 보다는 시작시간이 크고, 끝나는 시간이 가장 빠른 친구
        
        for (int j=0;j<=N;j++){ 
            if(meeting[j][0]<check){continue;} // check 시간 보다 시작 시간이 이르다면 스킵한다.
            else {
                
            }
            //체크 시간보다 시작 시간이 늦는 친구들중 끝나는 시간이 가장 빠른 친구를 선택

        }
            




    }
}