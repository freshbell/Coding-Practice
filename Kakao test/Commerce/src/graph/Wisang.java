package graph;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class Wisang {
    public static void main(String[] args) {
        int n = 10;
        int[][] fares = new int[9][3];
        int[] d = new int[n + 1];
        int[][] gap = new int[n+1][2];
        int[] costs = new int[n+1];

        Queue<Integer> queue = new LinkedList<>();
        ArrayList<Node2> [] arrayList = new ArrayList[n + 1];

        for(int i = 1 ; i <= fares.length ; i ++) {
            d[fares[i][1]] += 1;
            arrayList[fares[i][0]].add(new Node2(fares[i][1],fares[i][2]));
        }

        for(int i = 1 ; i <= d.length ; i ++) {
            if (d[i] == 0) {
                queue.add(i);
                gap[i][0] = costs[i - 1];
            } else gap[i][1] = costs[i-1];
        }

        int wich = 0;
        while(!queue.isEmpty()) {
            wich = queue.poll();

            for(int i = 0; i < arrayList[i].size() ; i ++) {
                int next = arrayList[wich].get(i).end;
                int multi = arrayList[wich].get(i).gap;

                gap[next][0] += gap[wich][0] * multi;
                gap[next][1] += gap[wich][1] * multi;

                d[next] --;
                if(d[next] == 0) queue.add(next);
            }
        }

        System.out.println(wich);
    }
}

class Node2 {
    int end;
    int gap;

    Node2(int end, int gap) {
        this.end = end;
        this.gap = gap;
    }
}
