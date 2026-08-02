const categories = [
  "Electronics",
  "Fashion",
  "Gaming",
  "Home",
  "Books",
  "Fitness",
  "Beauty",
  "Toys",
];

export default function Categories() {
  return (
    <section className="p-8 bg-gray-100">
      <h2 className="text-3xl font-bold mb-6">
        Shop by Category
      </h2>

      <div className="grid grid-cols-2 md:grid-cols-4 gap-5">
        {categories.map((category) => (
          <div
            key={category}
            className="bg-white p-8 rounded-lg shadow hover:shadow-lg cursor-pointer transition"
          >
            <h3 className="text-xl font-semibold">
              {category}
            </h3>
          </div>
        ))}
      </div>
    </section>
  );
}