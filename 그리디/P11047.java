package 그리디;
import java.util.Scanner;
// https://www.acmicpc.net/problem/11047
public class P11047 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); //N은 동전의 종류 갯수
        int K = sc.nextInt(); //K는 동전으로 만들 가치의 합
        int [] money = new int[N];

        for(int i = 0 ; i<N ; i++){ //동전의 종류를 저장하는 배열
            money[i] = sc.nextInt();
        }

        int count = 0;

        for(int i = N-1 ; i>=0;i--){
            if (money[i] <= K && (K/money[i]) > 0) {
                count += (K/money[i]);
                K = K%money[i];
            }
            
            if(K == 0){
                break;
            }
        }
        System.out.println(count);
    }
}
