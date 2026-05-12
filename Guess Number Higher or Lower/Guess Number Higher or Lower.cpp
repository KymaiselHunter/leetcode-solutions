/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

class Solution {
public:
    int guessNumber(int n) {
        int left = 1;
        int right = n;

        while(left < right)
        {
            
            int mid = (right - left) / 2 + left;
            cout << right << " " << left<< " " << mid << endl;
            int curr = guess(mid);
            cout << curr << endl;

            if(curr == -1) right = mid - 1;
            else if(curr == 1) left = mid + 1;
            else return mid;

        }

        return left;
    }
};