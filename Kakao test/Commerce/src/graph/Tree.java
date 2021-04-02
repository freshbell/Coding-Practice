package graph;

import java.util.ArrayList;

class Node4 {
    int data;
    ArrayList<Node4> childs;
}

class TreeNode {

    Node4 root;

    public Node4 getRoot() {
        return root;
    }

    public void setRoot(Node4 root) {
        this.root = root;
    }

    public TreeNode() {

    }

    public Node4 createNode(int data, ArrayList<Node4> childs) {
        Node4 node = new Node4();
        node.data = data;
        node.childs = childs;

        return node;
    }

    public void inOrder(Node4 node) {
        System.out.println(node.data);
        if(node.childs != null) {
            for (int i = 0; i < node.childs.size(); i++) {
                inOrder(node.childs.get(i));
            }
        }
    }
    public void preOrder(Node4 node) {
        if(node.childs != null) {
            for (int i = 0; i < node.childs.size(); i++) {
                inOrder(node.childs.get(i));
            }
        }
        System.out.println(node.data);
    }
}

public class Tree {
    public static void main(String[] args) {
        TreeNode treeNode = new TreeNode();
        Node4 n4 = treeNode.createNode(4,null);
        ArrayList<Node4> n5_childs = new ArrayList<Node4>();
        n5_childs.add(n4);
        Node4 n5 = treeNode.createNode(5,n5_childs);
        Node4 n2 = treeNode.createNode(2,null);
        Node4 n3 = treeNode.createNode(3,null);
        ArrayList<Node4> n1_childs = new ArrayList<Node4>();
        n1_childs.add(n2);
        n1_childs.add(n3);
        n1_childs.add(n5);
        Node4 n1 = treeNode.createNode(1,n1_childs);

        treeNode.setRoot(n1);
        treeNode.inOrder(treeNode.getRoot());
        treeNode.preOrder(treeNode.getRoot());
    }
}
