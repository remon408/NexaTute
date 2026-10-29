NexaTute — সব মকআপ ও প্রোটোটাইপ (স্ট্যাটিক ওয়েবসাইট)
NexaTute — all mockups and prototypes (static website)
=====================================================

বাংলা
-----
১. zip ফাইলটি আনজিপ করুন। ভেতরে "nexatute-mockups" নামে একটি ফোল্ডার পাবেন।
২. ব্রাউজারে app.netlify.com/drop খুলুন।
৩. পুরো "nexatute-mockups" ফোল্ডারটি টেনে এনে পাতার বক্সে ছেড়ে দিন (ভেতরের ফাইল আলাদা করে নয়, পুরো ফোল্ডার)।
   কয়েক সেকেন্ডে Netlify একটি লিংক দেবে, যেমন https://random-name-123.netlify.app
৪. সাইটটি স্থায়ীভাবে রাখতে Netlify অ্যাকাউন্টে লগ-ইন করুন (বা সাইটটি "claim" করুন)।
   লগ-ইন ছাড়া রাখা সাইট কিছু সময় পর মুছে যেতে পারে।
৫. নাম বদলাতে: Netlify-তে সাইটটি খুলুন → Site configuration → Site details → Change site name।
   নতুন নাম দিন (যেমন nexatute-mockups) — লিংক হবে https://nexatute-mockups.netlify.app
৬. পরে নতুন সংস্করণ দিতে: সাইটের Deploys পাতায় নতুন ফোল্ডারটি আবার টেনে ছেড়ে দিন।

জরুরি: লিংক যার কাছে আছে, সে-ই সাইটটি দেখতে পারবে। সার্চ ইঞ্জিনে যেন না আসে সেজন্য
robots.txt, "noindex" ট্যাগ ও _headers ফাইল দেওয়া আছে, কিন্তু এটি পাসওয়ার্ড-সুরক্ষা নয়।
লিংক শুধু যাদের দেখানো দরকার তাদেরই দিন।

শুরুর পাতা index.html (ওয়েবসাইট প্রিভিউ)। সব পাতার নিচে বাঁ কোণে "← সব পাতা / All pages" চাপলে
আবার শুরুর পাতায় ফেরা যায়। সব কিছু এই ফোল্ডারের ভেতরেই আছে (ফন্টসহ) — বাইরে থেকে কিছু লোড হয় না।

English
-------
1. Unzip the file. Inside is a folder named "nexatute-mockups".
2. Open app.netlify.com/drop in your browser.
3. Drag the whole "nexatute-mockups" folder onto the drop area (the folder itself, not the files inside it).
   After a few seconds Netlify gives you a link such as https://random-name-123.netlify.app
4. To keep the site permanently, log in to (or sign up for) a Netlify account, or "claim" the site when asked.
   A site dropped without an account may be deleted after a while.
5. To rename it: open the site in Netlify → Site configuration → Site details → Change site name.
   Enter a new name (for example nexatute-mockups) — the link becomes https://nexatute-mockups.netlify.app
6. To publish a new version later: on the site's Deploys page, drag the new folder onto it again.

Important: anyone who has the link can see the site. robots.txt, a "noindex" tag and the _headers file
keep it out of search engines, but this is not password protection. Share the link only with the people
who should see it.

The start page is index.html (the website preview). The "← সব পাতা / All pages" button at the bottom left
of every page takes you back to it. Everything is inside this folder (fonts included); nothing is loaded
from other websites.

Contents: index.html + one .html page per board, frames/ (phone and fixed-size boards), boards/ (board
data and logic), dc-runtime.js (our renderer), vendor/ (Preact, MIT), fonts/ (OFL), thumbs/ (thumbnails).
