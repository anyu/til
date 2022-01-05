# Static vs Dynamic Dispatch

- static dispatch = loosely correlates with use of generics for this purpose
- dynamic dispatch = use of trait objects

## Deciding between static vs. dynamic dispatch

**TLDR**

It depends.

Static dispatch may be more suitable for **libraries**, so  users of the library can decide what dispatch is best for them. With dynamic dispatch, users are forced to use dynamic dispatch as well. More performant due to use of inlining.

Dynamic dispatch may be more suitable for **binaries**, particularly in low-resource environments where a small binary size is important. Static dispatch results in larger binaries because it creates a copy of the same generic function for each type it's used with.

## Resources

> ...static dispatching of any method calls, allowing for inlining and hence usually higher performance. It also has some downsides: causing code bloat due to many copies of the same function existing in the binary, one for each type.
>
> Furthermore, compilers aren’t perfect and may “optimise” code to become slower. For example, functions inlined too eagerly will bloat the instruction cache (cache rules everything around us). This is part of the reason that #[inline] and #[inline(always)] should be used carefully, and one reason why using a dynamic dispatch is sometimes more efficient.
>
> However, the common case is that it is more efficient to use static dispatch, and one can always have a thin statically-dispatched wrapper function that does a dynamic, but not vice versa, meaning static calls are more flexible. The standard library tries to be statically dispatched where possible for this reason.
>
([Static and Dynamic Dispatch](https://www.cs.brandeis.edu/~cs146a/rust/doc-02-21-2015/book/static-and-dynamic-dispatch.html))

> When you’re given the choice between static and dynamic dispatch, there is rarely a clear-cut right answer. Broadly speaking, though, you’ll want to use static dispatch in your libraries and dynamic dispatch in your binaries. In a library, you want to allow your users to decide what kind of dispatch is best for them, since you don’t know what their needs are. If you use dynamic dispatch, they’re forced to do the same, whereas if you use static dispatch, they can choose whether to use dynamic dispatch or not.
>
(Rust for Rustaceans)



- [Rust By Example: Returning Traits with dyn](https://doc.rust-lang.org/rust-by-example/trait/dyn.html)
- [Don't use boxed trait objects](https://bennetthardwick.com/dont-use-boxed-trait-objects-for-struct-internals/)
