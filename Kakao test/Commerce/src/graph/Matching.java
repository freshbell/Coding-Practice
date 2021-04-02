package graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Vector;

public class Matching {
    public static Boolean dfs(int wich, Boolean[] chk, int[] d,ArrayList<Integer>[] arr) {
        for(int i = 0 ; i < arr[wich].size() ; i ++) {
            int next = arr[wich].get(i);

            if(chk[next] == true) continue;
            chk[next] = true;
            if(d[next] == 0 || dfs(d[next],chk,d,arr)) {
                d[next] = wich;
                return true;
            }
        }
        return false;
    }
    public static void main(String[] args) {
        int n = 6; // 노드
        int m = 4; // 간선
        int[] d = new int[n+1];
        int[][] fares = new int[][]{{1, 4}, {1, 6}, {2, 4}, {3, 5}};
        ArrayList<Integer>[] arr = new ArrayList[n+1];
        Boolean[] chk = new Boolean[n+1];

        Arrays.fill(arr,new ArrayList<Integer>());
        for(int i = 0 ; i < fares.length ; i ++) {
            int start = fares[i][0];
            int end = fares[i][1];

            arr[start].add(end);
        }

        int count = 0;
        for(int i = 1 ; i <= n/2 ; i ++) {
            Arrays.fill(chk,false);
            if(dfs(i,chk,d,arr)) count ++;
        }

        System.out.println(count);
    }
}
