async function getProduct(id: string) {
  const res = await fetch(
    `http://127.0.0.1:8000/products/${id}`,
    {
      cache: "no-store",
    }
  );

  return res.json();
}

export default async function ProductPage({
  params,
}: {
  params: Promise<{ id: string }>;
}) {
  const { id } = await params;

  const product = await getProduct(id);

  return (
    <main className="p-10 bg-gray-100 min-h-screen">
      <div className="max-w-6xl mx-auto bg-white p-8 rounded-lg shadow-lg grid md:grid-cols-2 gap-10">

        <img
          src={product.image}
          alt={product.title}
          className="w-full h-[500px] object-cover rounded"
        />

        <div>
          <h1 className="text-4xl font-bold">
            {product.title}
          </h1>

          <p className="text-gray-500 mt-4 text-lg">
            {product.description}
          </p>

          <p className="text-3xl font-bold text-yellow-600 mt-8">
            ${product.price}
          </p>

          <button className="bg-yellow-400 px-10 py-4 rounded-lg mt-8 font-bold hover:bg-yellow-500 transition">
            Add To Cart
          </button>
        </div>
      </div>
    </main>
  );
}