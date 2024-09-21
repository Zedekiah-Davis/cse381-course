/* CSE 381 - BetterLinearSerach
*  (c) BYU-Idaho - It is an honor code violation to post this
*  file completed in a public file sharing site. F4.
*
*  Instructions: Implement the Search function per the instructions
*  in the comments.  Run all tests in BetterLinearSearchTest.cs to verify your code.
*/

namespace AlgorithmLib;

public static class BetterLinearSearch
{

    /* Search for an item in a list.  Ignore duplicates by exiting
    *  as soon as the first match is found.
    *
    *  Inputs:
    *     data - list to search
    *     target - value to search for
    *  Outputs:
    *     Index where target was found
    *
    *  Note: Return -1 if target not found
    */
    public static int Search<T>(List<T> data, T target) where T : IComparable<T>
    {
        // Create incrementing loop which searches through data list
        for (int i = 0; i < data.Count; i++){
            // If the value of data is equal to target then return the index value
            if (data[i].Equals(target)) {
                return i;
            }
        }
        // If target value doesn't exist in data list then return -1
        return -1;
    }
}