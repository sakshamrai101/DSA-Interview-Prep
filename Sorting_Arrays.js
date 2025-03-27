function mergeSort (array, low, high) {

    let mid = Math.floor((low + high) / 2);

    // Base case: when we cannot divide the current array into smaller sublists
    if (low === high) return;

    mergeSort(array, low, mid);
    mergeSort(array, mid + 1, high);
    merge(array, low, mid, high);

}

function merge (array, low, mid, high) {
    let temp = [];

    let left = low;
    let right = mid + 1;

    // till I have elts on left and right
    while (left <= mid && right <= high) {
        // Put the smaller elts in temp and move pointer:
        if (array[left] <= array[right]) {
            temp.push(array[left]);
            left ++;
        }
        else {
            temp.push(array[right]);
            right++;
        }
    }

    // Copy remaining elts:
    while (left <= mid) {
        temp.push(array[left]);
        left ++;
    }
    while (right <= high) {
        temp.push(array[right]);
        right++;
    }

    // Copy elts from temp array to original array:
    for (let i = low; i <= high; i ++) {
        array[i] = temp[i - low];
    }

    // low = 2, high = 4;
    // array = [x, x, 3, 2, 1, x];
    // after merging, temp = [1, 2, 3], these must go into array[2] array[4]:
    // i = 2 -> array[2] -> temp[2 - 2] -> temp[0], so on and so forth
}

array = [4, 3, 0, 99, 1, 143, 44, 2, 3, 1, 2, 9, 10000];
mergeSort(array, 0, array.length - 1);
console.log(array);