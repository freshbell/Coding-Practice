package graph;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.Queue;

class Node3 implements Comparable<Node3>{

    int gap;
    int next;

    public Node3(int gap, int next) {
        this.gap = gap;
        this.next = next;
    }

    public int getGap() {
        return gap;
    }

    public int getNext() {
        return next;
    }

    public void setGap(int gap) {
        this.gap = gap;
    }

    public void setNext(int next) {
        this.next = next;
    }

    @Override
    public int compareTo(Node3 o) {
        if(this.getGap() > o.getGap()) return 1;
        else if (this.getGap() < o.getGap()) return -1;
        return 0;
    }
}

public class Dijkstra {
    public static void main(String[] args) {
        int n = 5; // 노드
        int m = 5; // 간선
        int start = 1;
        int[][] jido = {{1,2,3},{2,3,1},{3,4,4},{4,5,3},{3,5,100}};
        int[] d = new int[n+1];

        PriorityQueue<Node3> priorityQueue = new PriorityQueue<>();
        ArrayList<Node3>[] graph = new ArrayList[n+1];

        for(int i = 0 ; i <= n ; i ++) graph[i] = new ArrayList<Node3>();
        //Arrays.fill(graph,new ArrayList<Node3>());
        for(int i = 0 ; i < jido.length ; i ++ ) {
            graph[jido[i][0]].add(new Node3(jido[i][2], jido[i][1]));
            graph[jido[i][1]].add(new Node3(jido[i][2], jido[i][0]));
        }

        priorityQueue.add(new Node3(0,start));
        Arrays.fill(d,999);
        d[start] = 0;
        while(!priorityQueue.isEmpty()) {
            Node3 now = priorityQueue.peek();
            priorityQueue.poll();
            int now_wich = now.next;
            int now_cost = now.gap;

            if(now_cost > d[now_wich]) continue;

            for(int i = 0 ; i < graph[now_wich].size() ; i ++) {
                int cost = now_cost + graph[now_wich].get(i).gap;
                if (d[graph[now_wich].get(i).next] > cost) {
                    d[graph[now_wich].get(i).next] = cost;
                    priorityQueue.add(new Node3(cost, graph[now_wich].get(i).next));
                }
            }
        }

        for(int i = 0 ; i < d.length ; i ++)
            System.out.println(d[i]);
    }
}
