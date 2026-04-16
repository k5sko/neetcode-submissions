class MedianFinder {
    PriorityQueue<Integer> belowNegative;
    PriorityQueue<Integer> above;
    int size;
    double median;

    public MedianFinder() {
        belowNegative = new PriorityQueue<>();
        above = new PriorityQueue<>();
        median = Integer.MIN_VALUE;
        size = 0;
    }
    
    public void addNum(int num) {
        if (size == 0) {
            belowNegative.add(-1 * num);
            size++;
            median = num;
            return;
        }
        else if (size == 1) {
            belowNegative.add(-1 * num);
            int toInsert = -1 * belowNegative.poll();
            above.add(toInsert);
            size++;
            median = (toInsert + -1 * belowNegative.peek())/2.0;
            return;
        }
        int maxBelow = -1 * belowNegative.peek();
        int minAbove = above.peek();
        size++;

        if (num < median) {
            belowNegative.add(-1 * num);
        }
        else {
            above.add(num);
        }

        if (size%2 == 0) {
            if (belowNegative.size() > above.size()) {
                int toInsert = -1 * belowNegative.poll();
                above.add(toInsert);
            }
            else if (belowNegative.size() < above.size()) {
                int toInsert = above.poll();
                belowNegative.add(-1 * toInsert);
            }
            median = (-1 * belowNegative.peek() + above.peek())/2.0;
        }
        else {
            if (belowNegative.size() > above.size()) {
                median = -1 * belowNegative.peek();
            }
            else {
                median = above.peek();
            }
        }
    }

    /*
    * median     belowNegative      above    size
    * 5           -5                            1
    * 
    * 4            -3                  5        2
    *
    * 5           -3                  5         3
    *                               7
    * 4           -3                  5         4
    *           -2                  7
    */

    /* maxBelow        minAbove
    *   3                  5
    *   3                  5
    *
    */
    
    public double findMedian() {
        return median;
    }
}
