import java.io.*;
import java.util.*;

public class QuickSort{

	// just swap the index not the rea
	public static void swap(int A[], int x, int y){
		int temp = A[x];
		A[x] = A[y];
		A[y] = temp;
	}

	// partiton returns an integer represent the pivot
	public static int partition(int A[], int f, int l){

		int pivot = A[f];
		while(f<l){
			if( A[f] == pivot || A[l] == pivot){
				System.out.println("only distict integers allowed");
			}
			while (A[f] < pivot) f++;
			while (A[l] > pivot) l--;
			swap(A, f, l);

		}
		return f;
	}
	public static void Quicksort(int A[], int f, int l){
		if( f>= 1) return;
		int pivot_index = partition(A ,f ,l);
		Quicksort(A, f, pivot_index);
		Quicksort(A, pivot_index +1 , l);
	}

	public static void main(String argv[]){
		int A[] = new int[argv.length];
		for(int i=0; i <= argv.length; i++){
			A[i] = Interger.parseInt(argv[i]);

		}
		Quicksort(A,0 ,argv.length -1);
		for(int i=0; i< argv.length; i++) System.out.print(A[i] + " ");
	}
}