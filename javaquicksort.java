

int partition(int[] a, int left, int right){
	int i =left;
	int j =right;
	//pivot is the value of the mid_index
	int pivot = a[(left+right)/2];
	// left is always on the left side of right side
	while(i<= j){
		//find the index on the left side of pivot, whose value is larger than pivot 
		while(a[i]<pivot){
			i ++;
		}
		//find the index on the right side of pivot, whose value is smaller than pivot
		while(a[j] > pivot){
			j--;
		}
		//swap the a[i] and a[j]( a[i] > pivot, a[j] < pivot)
		int temp = a[i];
		a[i] = a[j];
		a[j] = temp;
		i++;
		j--;

	}
	return i;
}
public void quicksort(int[] a, int left, int right){
	int pivot_index = partition(a, left, right);
	if(left <= right){
		quicksort(a, left, pivot_index-1);
		quicksort(a, pivot_index+1, right);
	}
} 