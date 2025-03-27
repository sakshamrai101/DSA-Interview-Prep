class CustomArray {

    constructor(capacity) {
        this.capacity = capacity;
        this.length = 0;
        this.container = {} // In Js, arrays are key-value objects where keys are indices and values are elements at those indices. 
    }

    // Inserts elt at given index
    insert(index, element) {

        // Check for valid index:
        if (index < 0 || index > this.capacity) {
            return false;
        }

        // Check if array is full:
        if (this.capacity == this.length) {
            return false;
        }

        // First perform right shifting then perform insertion:
        for (let i = this.length; i > index; i--) {
            this.container[i] = this.container[i - 1];
        }
        this.container[index] = element;


        this.length += 1;
        return true;
    }

    // Inserts elt at the start of array
    prePend(element) {

        // Check if array is full:
        if (this.capacity == this.length) {
            this.reSize();
        }

        // Perform shifting towards the right:
        for (let i = this.length; i > 0; i--) {
            this.container[i] = this.container[i - 1];
        }

        // Insert at start:
        this.container[0] = element;
        this.length += 1;
        return true;
    }

    // Inserts elt at the end of the array
    append(element) {

        // Check if array capacity is full:
        if (this.length == this.capacity) {
            this.reSize();
        }

        // Insert at end:
        this.container[this.length] = element;
        this.length += 1;
        return true;
    }

    // Creates a new array 2*size of old array
    reSize() {
        // Create a new array with 2 * capapcity of old array:
        let newCapacity = 2 * this.capacity;
        let newContainer = {};

        // Copy the elts from old array to new array:
        for (let i = 0; i < this.length; i ++) {
            newContainer[i] = this.container[i];
        }

        // Change reference of old container to new container:
        this.container = newContainer;
        this.capacity = newCapacity;
    }

    // Finds the given elt and returns true or false 
    find(element) {
        for (let i = 0; i < this.length; i ++) {
            if (this.container[i] === element) {
                return true;
            }
        }
        return false;
    }

    // Removes the passed in elt
    remove(index) {
        
        // Check for valid index:
        if (index < 0 || index > this.length) {
            return false;
        }

        var element = this.container[index];

        // Shift all elements from index to length 1 behind.
        for (let i = index; i < this.length - 1; i ++) {
            this.container[i] = this.container[i + 1];
        }

        delete this.container[this.length - 1];
        this.length -= 1;
        return element;
    }

    // Returns the current size of the array
    getSize() {
        return this.length;
    }

    getCapacity() {
        return this.capacity;
    }

    binarySearch(element) {

        // declare terminal pointers:
        var L = 0;
        var R = this.length - 1;

        // loop indefintely:
        while (L <= R) {
            
            // get the middle element:
            let m = Math.floor((L + R)/ 2);

            if (this.container[m] === element) {
                return true;
            }
            else if (this.container[m] < element) {
                L = m + 1;
            }

            else {
                R = m - 1;
            }
        }
        return false;

    }

}


const myArr = new CustomArray(5);
myArr.append(4);
myArr.append(19);
myArr.append(922);
myArr.append(67);
myArr.append(333);
myArr.append(0);


// Some problems based on BS:


// smallest missing number in sorted array 
function smallestMissingNumber (nums) {

    // declare pointers:
    var l = 0;
    var r = nums.length - 1;

    while (l <= r) {
        var m = Math.floor((l + r) / 2);

        if (m === nums[m]) {
            l = m + 1;
        }
        else if (m < nums[m]) {
            r = m - 1;
        } 
    }

    return l;
}


function partition (array, l, h) {
    
    // declare pointers to swap larger and greater values than pivot:
    var pivot = array[l];
    var i = l;
    var j = h;

    while (i < j) {

        // find first larger element than pivot:
        while (array[i] <= pivot && i < h) {
            i ++;
        }

        // find the first smallest element than pivot:
        while (array[j] > pivot && j > l) {
            j--;
        }

        // swap larger and smaller element:
        if (i < j) {
            let temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }

    }

    // Swap pivot element with j value:
    let temp = array[l];
    array[l] = array[j];
    array[j] = temp;
    return j;
}

function quickSort(array, l, h) {
    if (l < h) {
        let pivot = partition(array, l, h);
        quickSort(array, l, pivot - 1);
        quickSort(array, pivot + 1, h);
    }
}



function mergeSort (array, low, high) {

    // while there are elements:
    if (low === high) {
        return;
    }
    let mid = Math.floor((low + high) / 2);
    mergeSort(array, low, mid);
    mergeSort(array, mid + 1, high);
    merge(array, low, mid, high);
}

function merge (array, low, mid, high) {
    let temp = [];
    let l = low;
    let r = mid + 1;


    // till I have elts on left and right. 
    while (l <= mid && r <= high) {
        

        // Add the smaller elts first to temp
        if (array[l] <= array[r]) {
            temp.push(array[l]);
            l++;
        }
        else {
            temp.push(array[r]);
            r++;
        }

    }

    // Copy remaining elements from right and left. 
    while (l <= mid) {
        temp.push(array[l]);
        l++;
    }

    while (r <= high) {
        temp.push(array[r]);
        r++;
    }

    // Copy elements from temp to original array:
    for (let i = low; i <= high; i++) {
        array[i] = temp[i - low];
    }
}

let array = [5, 1, 0, 92, 15, 2, 4, 3, 2, 5, 1, 0, 55];
mergeSort(array, 0, array.length - 1);
console.log(array);