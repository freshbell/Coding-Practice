package graph;

class TrieNode {
    TrieNode[] next;
    boolean leaf;

    public TrieNode() {
        this.next = new TrieNode[26];
        this.leaf = false;
    }

    void insert(String string) {
        char[] s = string.toCharArray();
        char curr = s[0];

        if(curr == '\0')
            leaf = true;
        else {
            int idx = char2idx(curr);
            if(next[idx] == null) next[idx] = new TrieNode();
            if(string.length() > 1) string = string.substring(1);
            next[idx].insert(string);
        }
    }

    Boolean find(String string) {
        char[] s = string.toCharArray();
        char curr = s[0];

        if(curr == '\0') return leaf;
        else {
            int idx = char2idx(curr);
            if(next[idx] == null) return null;
            if(string.length() > 1) string = string.substring(1);

            return next[idx].find(string);
        }
    }

    private int char2idx(char c) {
        if(c < 'a') {
            c += ('a' - 'A');
        }

        return c - 'a';
    }
}

public class Trie {
    private TrieNode root = new TrieNode();

    private void insert(String key) {
        root.insert(key + '\0');
    }

    private void find(String key) {
        Boolean result = root.find(key + '\0');

        if(result == null) System.out.println("값이 없음");
        else if (result) System.out.println("값이 있음");
        else System.out.println("값이 있으나 끝이 아님");
    }
    public static void main(String[] args) {
        Trie trie = new Trie();
        trie.insert("Hello");
        trie.insert("House");

        trie.find("Hous");
        trie.find("Hell");
        trie.find("Horse");
    }
}
