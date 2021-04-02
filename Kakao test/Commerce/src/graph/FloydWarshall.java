package graph;

public class FloydWarshall {
    public static void main(String[] args) {
        int n = 10; // 노드
        int m = 10; // 간선
        int s=1, a=2, b=3; // 시작점, 도착점 A, B
        int[][] fares = new int[m][3];

        solution(n,s,a,b,fares);
    }

    public static int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = 0;
        int[][] map = new int[n+1][n+1];

        for(int i = 1 ; i <= n ; i ++)
            for(int j = 1 ; j <= n ; j ++) {
                if(i ==j) map[i][j] = 0;
                else map[i][j] = 9999999;
            }

        for(int i = 0 ; i < fares.length ; i ++ ) {
            int x = fares[i][0];
            int y = fares[i][1];
            int gap = fares[i][2];

            map[x][y] = gap;
            map[y][x] = gap;
        }

        for(int k = 1 ; k <= n ; k ++) {
            for(int i = 1 ; i <= n ; i ++ ) {
                for(int j = 1 ; j <= n ; j ++) {
                    map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
                }
            }
        }

        int minimum = 9999999;
        for(int i = 1 ; i <= n ; i ++) {
            minimum = Math.min(minimum,map[s][i] + map[i][a] + map[i][b]);
        }
        answer = minimum;
        return answer;
    }
}
