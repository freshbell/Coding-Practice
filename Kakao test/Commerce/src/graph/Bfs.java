package graph;

import java.util.LinkedList;
import java.util.Queue;

class Node{
    int x;
    int y;

    Node(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class Bfs {
    public static void main(String[] args) {

    }

    public static void bfs(int start, int end) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(start, end));
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};

        while(!queue.isEmpty()) {
            Node node = queue.poll();

            for(int i = 0 ; i < 4 ; i ++) {
                int xx = node.x + dx[i];
                int yy = node.y + dy[i];
                if(0 <= xx && xx < 10 && 0 <= yy && yy < 10) {
                    queue.add(new Node(xx,yy));
                }
            }
        }
    }
}
