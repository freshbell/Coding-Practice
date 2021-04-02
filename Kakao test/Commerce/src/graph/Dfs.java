package graph;

public class Dfs {

    static int N = 10, M = 10;
    static int maximum = 9999;
    static boolean[][] chk = new boolean[N][M];
    static int[][] map = new int[N][M];

    public static void main(String[] args) {
        int i, j;

        for(i = 0 ; i < N ; i ++)
            for(j = 0 ; j < M ; j ++) chk[i][j] = false;
        dfs(0,0,0);
    }

    public static void dfs(int x, int y, int count) {
        if (x == N && y == M) maximum = Math.min(maximum, count);
        else {
            chk[x][y] = true;
            int[] dx = {0, 1, 0, -1};
            int[] dy = {1, 0, -1, 0};

            for (int i = 0; i < 4; i++) {
                int xx = x + dx[i];
                int yy = y + dy[i];

                if (!(0 <= xx && xx < N && 0 <= yy && y < M && map[xx][yy] == 0 && chk[xx][yy] == false)) continue;
                dfs(xx, yy, count + 1);
                chk[xx][yy] = false;
            }
        }
    }
}
