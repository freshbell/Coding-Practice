package graph;

import java.util.HashMap;

class TreeBin {
    TreeBin treeBin;
    int data;
    int left;
    int right;

    public TreeBin getTreeBin() {
        return treeBin;
    }

    public void setTreeBin(TreeBin treeBin) {
        this.treeBin = treeBin;
    }

    TreeBin(int data, int left, int right) {
        this.data = data;
        this.left = left;
        this.right = right;
    }

    // 중위 순회
    public void inOrder(TreeBin treeBin, HashMap<Integer, TreeBin> hashMap) {
        if(treeBin != null) {
            if (treeBin.left != 0) inOrder(hashMap.get(treeBin.left), hashMap);
            System.out.println(treeBin.data);
            if (treeBin.right != 0) inOrder(hashMap.get(treeBin.right), hashMap);
        }
    }
    // 전위 순회
    public void preOrder(TreeBin treeBin, HashMap<Integer, TreeBin> hashMap) {
        if(treeBin != null) {
            System.out.println(treeBin.data);
            if (treeBin.left != 0) preOrder(hashMap.get(treeBin.left), hashMap);
            if (treeBin.right != 0) preOrder(hashMap.get(treeBin.right), hashMap);
        }
    }
    // 후위 순회
    public void postOrder(TreeBin treeBin, HashMap<Integer, TreeBin> hashMap) {
        if(treeBin != null) {
            if (treeBin.left != 0) postOrder(hashMap.get(treeBin.left), hashMap);
            if (treeBin.right != 0) postOrder(hashMap.get(treeBin.right), hashMap);
            System.out.println(treeBin.data);
        }
    }
}

public class BinTree {
    public static void main(String[] args) {

        int[][] graph = {{1,2,3},{2,4,5},{3,6,7},{4,9,0},{9,0,0},{5,0,0},{6,0,0},{7,0,0}};

        HashMap<Integer, TreeBin> hashMap = new HashMap<Integer,TreeBin>();
        TreeBin treeBin = null;

        for (int i = 0 ; i < graph.length ; i ++) {
            int data = graph[i][0];
            int left = graph[i][1];
            int right = graph[i][2];
            treeBin = new TreeBin(data,left,right);
            hashMap.put(data,treeBin);
        }

        treeBin.inOrder(hashMap.get(1), hashMap);
        treeBin.preOrder(hashMap.get(1), hashMap);
        treeBin.postOrder(hashMap.get(1), hashMap);
    }
}
