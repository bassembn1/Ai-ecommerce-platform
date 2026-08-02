export default function Hero() {
  return (
    <section className="relative">
      <img
        src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3"
        alt="hero"
        className="w-full h-[400px] object-cover"
      />

      <div className="absolute inset-0 bg-black/30" />

      <div className="absolute top-1/2 left-10 -translate-y-1/2 text-white">
        <h1 className="text-5xl font-bold">
          Welcome to BNG
        </h1>

        <p className="text-xl mt-3">
          Shop millions of products
        </p>

        <button className="bg-purple-400 text-black px-6 py-3 rounded-md mt-5 font-semibold hover:scale-105 transition">
          Shop Now
        </button>
      </div>
    </section>
  );
}