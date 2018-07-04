#include <stdio.h>
#include <iostream>

using namespace std;

void swap(int *x, int *y)
{
	int temp = *x;
	*x = *y;
	*y = temp;
}

class MinHeap{
	int *harr;
	int capacity;
	int heap_size;
public:
	MinHeap(int a[], int size);
	void buildHeap();
	void MinHeapify(int i);
	int parent(int i)  { return (i-1)/2;  }
    int left(int i)    { return (2*i + 1);  }
    int right(int i)   { return (2*i + 2);  }
    int extractMin();  // extracts root (minimum) element
    int getMin()       {  return harr[0]; }
 
    // to replace root with new node x and heapify() new root
    void replaceMin(int x) { harr[0] = x; MinHeapify(0); }
}

MinHeap::MinHeap(int a[], in size)
{
	heap_size=size;
	harr = a;
}

void MinHeap::buildHeap()
{
	for(int i = (heap_size - 1)/2; i >= 0; i--)
		MinHeapify(i);
}

// Method to remove minimum element (or root) from min heap
int MinHeap::extractMin()
{
    if (heap_size == 0)
        return INT_MAX;
 
    // Store the minimum vakue.
    int root = harr[0];
 
    // If there are more than 1 items, move the last item to root
    // and call heapify.
    if (heap_size > 1)
    {
        harr[0] = harr[heap_size-1];
        MinHeapify(0);
    }
    heap_size--;
 
    return root;
}
 
// A recursive method to heapify a subtree with root at given index
// This method assumes that the subtrees are already heapified
void MinHeap::MinHeapify(int i)
{
    int l = left(i);
    int r = right(i);
    int smallest = i;
    if (l < heap_size && harr[l] < harr[i])
        smallest = l;
    if (r < heap_size && harr[r] < harr[smallest])
        smallest = r;
    if (smallest != i)
    {
        swap(&harr[i], &harr[smallest]);
        MinHeapify(smallest);
    }
}
 
// A utility function to swap two elements
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
 
// Function to return k'th largest element from input stream
void kthLargest(int k)
{
    // count is total no. of elements in stream seen so far
    int count = 0, x;  // x is for new element
 
    // Create a min heap of size k
    int *arr = new int[k];
    MinHeap mh(arr, k);
 
 
    while (1)
    {
        // Take next element from stream
        cout << "Enter next element of stream ";
        cin >> x;
 
        // Nothing much to do for first k-1 elements
        if (count < k-1)
        {
            arr[count] = x;
            count++;
        }
 
        else
        {
          // If this is k'th element, then store it
          // and build the heap created above
          if (count == k-1)
          {
              arr[count] = x;
              mh.buildHeap();
          }
 
          else
          {
               // If next element is greater than 
               // k'th largest, then replace the root
               if (x > mh.getMin())
                  mh.replaceMin(x); // replaceMin calls 
                                    // heapify()
          }
 
          // Root of heap is k'th largest element
          cout << "K'th largest element is "
               << mh.getMin() << endl;
          count++;
        }
    }
}
 
// Driver program to test above methods
int main()
{
    int k = 3;
    cout << "K is " << k << endl;
    kthLargest(k);
    return 0;
}
