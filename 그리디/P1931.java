package 그리디;
import java.util.Scanner;

public class P1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int [][] meeting = new int[N][2]; //0번째 열은 시작 시간, 1번째 열은 끝나는 시간
        int check = 0; // 회의실 마지막 사용 시간 체크
        int fast = 0;
        int count = 0; // 회의의 갯수
        

        for (int i=0 ; i<=N ; i++){ // 입력 받기 수행
            meeting[N][0] = sc.nextInt();
            meeting[N][1] = sc.nextInt();
        }
        //회의실 배정
        // 1. check 시간 보다는 시작시간이 크고, 끝나는 시간이 가장 빠른 친구
        fast = meeting[0][1]; //끝나는 시간 암거나 배정
        while(true){
        for (int j=0;j<=N;j++){ 
            if(meeting[j][0]<check){ // check 시간보다 시작 시간이 이르다면 스킵한다.
                continue;
            } 
            else if(fast>meeting[j][1]) {  // 끝나는 시간이 가장 빠른 친구를 선택
                fast = meeting[j][1]; // 끝나는 시간이 더 빠른 회의 시간을 fast에 할당
                check = fast;
            }
        
        }
        count++;
    }
}
}