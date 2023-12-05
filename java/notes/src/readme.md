## Notes
#### Wrapper Classes in Java
- `Wrapper classes` convert primitive data types into objects. Why into objects? Because objects are more widely used in Java.

#### User Inputs
- `BufferedReader` is more flexible as we can specify the size of stream input to be read. It is synchronized, therefore preferred with multiple threading.
- `Scanner` is good for decent input, and easy readability. It is slower than `BufferedReader`.
- `System.out.println()` is a perfect example of `Method Overloading` in Java.  Therefore, it can read all the data types. `read()` on the other hand can only read text.
- `System.out.println()` is synchronized and therefore slow when multiple threads are passed. Alternatives are `PrintWriter` or `BufferedWriter` class.

#### Enhanced Loop
- Enhanced for loop provides a simpler way to iterate through the elements of a collection or array. It is inflexible and should be used only when there is a need to iterate through the elements in a sequential manner without knowing the index of the currently processed element.
- The object/variable is immutable when enhanced for loop is used i.e it ensures that the values in the array can not be modified, so it can be said as a read-only loop where you can’t update the values as opposed to other loops where values can be modified.

#### Label
- A Label is used to identifies a block of code. Label name can be used to use break out of it.