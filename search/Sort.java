// COSC-311 Fall 2019
// HW1
// September 6, 2019

public class Sort {

    //sorts an array of ints using mergesort
    public void mergeSort(int[] to_sort) {
	int[] temp = new int[to_sort.length];
	mergeSort(to_sort, temp, 0, to_sort.length - 1);
    }

    //recursive helper method for mergesort
    public void mergeSort(int[] to_sort, int[] temp_array, int low, int high) {

	if(low < high) {	    
	    int mid = (low + high) / 2;
	    
	    mergeSort(to_sort, temp_array, low, mid);
	    mergeSort(to_sort, temp_array, mid + 1, high);
	    merge(to_sort, temp_array, low, mid, high);
	}

    }

    //merges two sorted subarrays (from low to mid and from mid+1 to high)
    public void merge(int[] to_sort, int[] temp, int low, int mid, int high){
	
	//copy values from low to high into temporary array
	for(int i = low; i <= high; i++) {
	    temp[i] = to_sort[i];
	}

	//copy smaller of left and right values back to to_sort
	int left_ctr = low;
	int right_ctr = mid + 1;
	int copy_ctr = low;

	while(left_ctr <= mid && right_ctr <= high) {
	    if(temp[left_ctr] < temp[right_ctr]) {
		to_sort[copy_ctr] = temp[left_ctr];
		left_ctr++;
	    }
	    else {
		to_sort[copy_ctr] = temp[right_ctr];
		right_ctr++;
	    }
	    copy_ctr++;
	}

	//if left_ctr hit mid before right_ctr hit high, then we're done
	//because remaining elements on the right side stay where they were
	//in the original array
	//otherwise need to copy rest of values before mid
	while(left_ctr <= mid) {
	    to_sort[copy_ctr] = temp[left_ctr];
	    left_ctr++;
	    copy_ctr++;
	}

    }


    // sorts an array of ints using insertion sort
    public void insertionSort(int[] to_sort) {
	
	int n = to_sort.length;

	for(int i = 1; i < n; i++) {

	    int val = to_sort[i];
	    int j = i - 1;

	    // insert the element that was at position i
	    // into sorted order in the range [0..i]
	    while(j >= 0 && val < to_sort[j]) {
		to_sort[j + 1] = to_sort[j];
		j--;
	    }

	    to_sort[j+1] = val;

	}

    }

    // sorts an array of ints using bubble sort
    public void bubbleSort(int[] to_sort) {
	int n = to_sort.length;

	for(int i = 0; i < n; i++) {

	    for(int j = 1; j < n - i; j++) {

		if(to_sort[j-1] > to_sort[j]) {
		    int temp = to_sort[j-1];
		    to_sort[j-1] = to_sort[j];
		    to_sort[j] = temp;
		}

	    } 

	} 

    }


    public static void main(String[] args) {
	// add whatever code you need to run your experiments
    }

}