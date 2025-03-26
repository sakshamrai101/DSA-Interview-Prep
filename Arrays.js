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
myArr.append(1);
myArr.append(2);
myArr.append(3);
myArr.append(4);
myArr.append(5);
myArr.append(6);


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


console.log(smallestMissingNumber([0, 1, 2, 3, 4, 6]));