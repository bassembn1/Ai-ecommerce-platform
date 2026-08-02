"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";

type Product = {
  id: number;
  title: string;
  price: number;
};

export default function AdminPage() {
  const [products, setProducts] = useState<Product[]>([]);

  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [price, setPrice] = useState("");
  const [image, setImage] = useState("");

  const token = typeof window !== "undefined"
    ? localStorage.getItem("token")
    : null;

  const router = useRouter();

useEffect(() => {
  const token = localStorage.getItem("token");

  if (!token) {
    router.push("/auth/login");
  }
}, []);

  async function fetchProducts() {
    const res = await fetch("http://127.0.0.1:8000/admin/products", {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    const data = await res.json();
    setProducts(data);
  }

  useEffect(() => {
    fetchProducts();
  }, []);

  async function handleAddProduct() {
    await fetch("http://127.0.0.1:8000/products", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        title,
        description,
        price: Number(price),
        image,
      }),
    });

    fetchProducts();
  }

  async function handleDelete(id: number) {
    await fetch(`http://127.0.0.1:8000/products/${id}`, {
      method: "DELETE",
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });

    fetchProducts();
  }

  return (
    <main className="p-10 bg-gray-100 min-h-screen">

      <h1 className="text-4xl font-bold mb-8">
        Admin Dashboard
      </h1>

      {/* Add Product */}
      <div className="bg-white p-6 rounded shadow mb-10">
        <h2 className="text-2xl font-bold mb-4">
          Add Product
        </h2>

        <input placeholder="Title" className="border p-2 w-full mb-2" onChange={(e) => setTitle(e.target.value)} />
        <input placeholder="Description" className="border p-2 w-full mb-2" onChange={(e) => setDescription(e.target.value)} />
        <input placeholder="Price" className="border p-2 w-full mb-2" onChange={(e) => setPrice(e.target.value)} />
        <input placeholder="Image" className="border p-2 w-full mb-2" onChange={(e) => setImage(e.target.value)} />

        <button onClick={handleAddProduct} className="bg-yellow-400 px-6 py-2 font-bold">
          Add Product
        </button>
      </div>

      {/* Products List */}
      <div>
        <h2 className="text-2xl font-bold mb-4">
          All Products
        </h2>

        <div className="grid md:grid-cols-3 gap-4">
          {products.map((p) => (
            <div key={p.id} className="bg-white p-4 rounded shadow">
              <h3 className="font-bold">{p.title}</h3>
              <p>${p.price}</p>

              <button
                onClick={() => handleDelete(p.id)}
                className="bg-red-500 text-white px-3 py-1 mt-3"
              >
                Delete
              </button>
            </div>
          ))}
        </div>
      </div>

    </main>
  );
}