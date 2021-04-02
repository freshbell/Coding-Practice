package graph;

import java.util.Arrays;

public class BinarySearch {
    public static int binarySearch(int[] arr, int start, int end, int want) {

        while(start <= end) {
            int mid = (start + end) / 2;

            if(arr[mid] == want) return mid;
            else if (arr[mid] > want) end = mid - 1;
            else start = mid + 1;
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {122,5,13,55,56,3,23};
        int want = 4;

        Arrays.sort(arr);
        int wich = binarySearch(arr,0,arr.length, want);
        if (wich == -1) System.out.println("Not Found");
        else System.out.println(wich);
    }
}
