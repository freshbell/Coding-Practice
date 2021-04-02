package graph;

import java.util.Collections;
import java.util.PriorityQueue;

public class Priority{
    public static void main(String[] args) {
        PriorityQueue<Integer> priorityQueue = new PriorityQueue<>();
        PriorityQueue<Integer> priorityQueueRev = new PriorityQueue<>(Collections.reverseOrder());

        priorityQueue.add(1);
        priorityQueue.add(3);
        priorityQueue.add(2);
        priorityQueue.add(5);
        priorityQueue.add(4);

        while(!priorityQueue.isEmpty()) {
            System.out.println(priorityQueue.peek());
            priorityQueue.poll();
        }
    }
}
