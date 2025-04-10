<template>
  <div
    class="min-h-screen bg-gradient-to-b from-gray-900 via-gray-900 to-purple-600 relative overflow-hidden"
  >
    <!-- Background gradient -->
    <div class="absolute inset-0 bg-purple-600"></div>

    <!-- Main content container -->
    <div
      class="relative z-10 flex items-center justify-center min-h-screen p-4"
    >
      <div class="w-full max-w-md mx-auto">
        <!-- Welcome text -->
        <div class="text-center mb-8 text-white">
          <h1 class="text-3xl md:text-4xl font-semibold mb-2">
            {{ isSignUp ? "Join us today" : "Welcome back" }}
          </h1>
          <p class="text-gray-300">
            {{
              isSignUp
                ? "Create your account to get started."
                : "Enter your personal details and start your journey with us."
            }}
          </p>
        </div>

        <!-- Auth form -->
        <div class="bg-white rounded-2xl shadow-xl p-8">
          <div class="mb-6 text-center">
            <h3 class="text-2xl font-bold text-gray-800">
              {{ isSignUp ? "Sign Up" : "Sign In" }}
            </h3>
            <p class="text-gray-500 mt-1">
              {{
                isSignUp ? "Already have an account?" : "Don't have an account?"
              }}
              <button
                @click="isSignUp = !isSignUp"
                class="text-purple-600 hover:text-purple-700 font-medium"
              >
                {{ isSignUp ? "Sign In" : "Sign Up" }}
              </button>
            </p>
          </div>

          <!-- Form fields -->
          <form @submit.prevent="handleSubmit">
            <div class="space-y-4">
              <!-- Name (only for sign up) -->
              <div v-if="isSignUp">
                <label class="block text-gray-700 text-sm font-medium mb-1"
                  >Full Name</label
                >
                <input
                  v-model="name"
                  type="text"
                  placeholder="John Doe"
                  class="w-full px-4 py-3 text-gray-700 bg-gray-100 rounded-lg focus:bg-white focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
                />
              </div>

              <!-- Email -->
              <div>
                <label class="block text-gray-700 text-sm font-medium mb-1"
                  >Email</label
                >
                <input
                  v-model="email"
                  type="email"
                  placeholder="your@email.com"
                  class="w-full px-4 py-3 text-gray-700 bg-gray-100 rounded-lg focus:bg-white focus:outline-none focus:ring-2 focus:ring-purple-500 transition"
                />
              </div>

              <!-- Password -->
              <div>
                <label class="block text-gray-700 text-sm font-medium mb-1"
                  >Password</label
                >
                <div class="relative">
                  <input
                    :type="showPassword ? 'text' : 'password'"
                    v-model="password"
                    placeholder="••••••••"
                    class="w-full px-4 py-3 text-gray-700 bg-gray-100 rounded-lg focus:bg-white focus:outline-none focus:ring-2 focus:ring-purple-500 pr-10 transition"
                  />
                  <button
                    type="button"
                    @click="showPassword = !showPassword"
                    class="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-purple-700"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      class="h-5 w-5"
                      fill="none"
                      viewBox="0 0 24 24"
                      stroke="currentColor"
                    >
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
                      />
                      <path
                        stroke-linecap="round"
                        stroke-linejoin="round"
                        stroke-width="2"
                        d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"
                      />
                    </svg>
                  </button>
                </div>
              </div>

              <!-- Remember me & Forgot password (Sign In only) -->
              <div class="flex items-center justify-between" v-if="!isSignUp">
                <label class="flex items-center text-gray-700 text-sm">
                  <input
                    type="checkbox"
                    class="rounded text-purple-600 focus:ring-purple-500"
                  />
                  <span class="ml-2">Remember me</span>
                </label>
                <a
                  href="#"
                  class="text-sm text-purple-600 hover:text-purple-700"
                >
                  Forgot password?
                </a>
              </div>

              <!-- Submit -->
              <button
                type="submit"
                class="w-full mt-6 bg-purple-600 hover:bg-purple-700 text-white py-3 rounded-lg font-semibold shadow-md transition duration-300"
              >
                {{ isSignUp ? "Create Account" : "Sign In" }}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>

    <!-- Wave effect -->
    <svg
      class="absolute bottom-0 left-0 w-full"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 1440 320"
    >
      <path
        fill="#fff"
        fill-opacity="1"
        d="M0,0L40,42.7C80,85,160,171,240,197.3C320,224,400,192,480,154.7C560,117,640,75,720,74.7C800,75,880,117,960,154.7C1040,192,1120,224,1200,213.3C1280,203,1360,149,1400,122.7L1440,96L1440,320L1400,320C1360,320,1280,320,1200,320C1120,320,1040,320,960,320C880,320,800,320,720,320C640,320,560,320,480,320C400,320,320,320,240,320C160,320,80,320,40,320L0,320Z"
      ></path>
    </svg>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const isSignUp = ref(false);
const showPassword = ref(false);

const name = ref("");
const email = ref("");
const password = ref("");

const handleSubmit = () => {
  if (isSignUp.value) {
    console.log("Sign Up:", {
      name: name.value,
      email: email.value,
      password: password.value,
    });
    // call your signup API here
  }
};
</script>
