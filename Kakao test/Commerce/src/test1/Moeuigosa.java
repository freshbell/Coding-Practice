package test1;

import java.util.ArrayList;

public class Moeuigosa {
    public static int[] solution(int[] answers) {
        int[] first = {1,2,3,4,5};
        int[] second = {2,1,2,3,2,4,2,5};
        int[] third = {3,3,1,1,2,2,4,4,5,5};
        int[] su = {5,8,10};
        int[] cor = {0,0,0};
        int[] answer = {};
        ArrayList<Integer> answer2 = new ArrayList<Integer>();

        int maximum = 0;

        for(int i = 0 ; i < answers.length ; i ++) {
            if (answers[i] == first[i % su[0]]) cor[0] += 1;
            if (answers[i] == second[i % su[1]]) cor[1] += 1;
            if (answers[i] == third[i % su[2]]) cor[2] += 1;
            if (maximum < cor[0]) maximum = cor[0];
            if (maximum < cor[1]) maximum = cor[1];
            if (maximum < cor[2]) maximum = cor[2];
        }

        for(int i = 0 ; i <= 2 ; i ++)
            if (maximum == cor[i]) answer2.add(i+1);

        answer = new int[answer2.size()];
        for(int i = 0 ; i < answer2.size() ; i ++)
            answer[i] = answer2.get(i);

        return answer;
    }

    public static void main(String[] args) {
        int[] answers = {1,3,2,4,2};
        int[] a;
        a = solution(answers);

        for(int i = 0 ; i < a.length ; i ++ ) {
            System.out.println(a[i]);
        }
    }
}