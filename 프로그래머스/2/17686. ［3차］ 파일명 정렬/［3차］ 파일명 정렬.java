import java.util.*;
class Solution {
    static List<File> fileList = new ArrayList<>();
    static class File implements Comparable<File> {
        String origin;
        String head;
        String number;
        String tail;
        int num;
        int idx;

        public File(String file, int idx) {
            extract(file);
            this.idx = idx;
        }

        private void extract(String file) {
            StringBuilder origin = new StringBuilder();
            StringBuilder head = new StringBuilder();
            StringBuilder number = new StringBuilder();
            StringBuilder tail = new StringBuilder();

            for (int i = 0; i < file.length(); i++) {
                char c = file.charAt(i);
                if (!Character.isDigit(c) && number.length() == 0) {
                    origin.append(c);
                    head.append(Character.toUpperCase(c));
                } else if (Character.isDigit(c) && tail.length() == 0) {
                    number.append(c);
                } else {
                    tail.append(c);
                }
            }
            
            this.origin = origin.toString();
            this.head = head.toString();
            this.number = number.toString();
            this.tail = tail.toString();
            this.num = Integer.parseInt(this.number);
        }

        @Override
        public int compareTo(File other) {
            int headCompare = this.head.compareTo(other.head);
            if (headCompare != 0) {
                return headCompare;
            }
            int numCompare = Integer.compare(this.num, other.num);
            if (numCompare != 0) {
                return numCompare;
            }
            return Integer.compare(this.idx, other.idx);
        }

        @Override
        public String toString() {
            return this.origin + this.number + this.tail;
        }
    }

    public String[] solution(String[] files) {
        for (int i = 0; i < files.length; i++) {
            fileList.add(new File(files[i], i));
        }

        Collections.sort(fileList);

        String[] answer = new String[files.length];
        for (int i = 0; i < files.length; i++) {
            answer[i] = fileList.get(i).toString();
        }

        return answer;
    }
}
