import Navbar from "@/src/components/navbar/Navbar";
import Hero from "@/src/components/home/Hero";
import Categories from "@/src/components/home/Categories";
import Products from "@/src/components/home/Products";

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <Categories />
      <Products />
    </main>
  );
}