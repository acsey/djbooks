CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE TABLE IF NOT EXISTS "account_emailconfirmation" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "created" datetime NOT NULL, "sent" datetime NULL, "key" varchar(64) NOT NULL UNIQUE, "email_address_id" integer NOT NULL REFERENCES "account_emailaddress" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "account_emailconfirmation_email_address_id_5b7f8c58" ON "account_emailconfirmation" ("email_address_id");
CREATE TABLE IF NOT EXISTS "account_emailaddress" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "verified" bool NOT NULL, "primary" bool NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "email" varchar(254) NOT NULL UNIQUE);
CREATE INDEX "account_emailaddress_user_id_2c513194" ON "account_emailaddress" ("user_id");
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0), "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_time" datetime NOT NULL);
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "last_name" varchar(150) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "first_name" varchar(150) NOT NULL);
CREATE TABLE IF NOT EXISTS "taggit_taggeditem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" integer NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "tag_id" integer NOT NULL REFERENCES "taggit_tag" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "taggit_taggeditem_object_id_e2d7d1df" ON "taggit_taggeditem" ("object_id");
CREATE INDEX "taggit_taggeditem_content_type_id_9957a03c" ON "taggit_taggeditem" ("content_type_id");
CREATE INDEX "taggit_taggeditem_tag_id_f4f5b767" ON "taggit_taggeditem" ("tag_id");
CREATE INDEX "taggit_taggeditem_content_type_id_object_id_196cc965_idx" ON "taggit_taggeditem" ("content_type_id", "object_id");
CREATE UNIQUE INDEX "taggit_taggeditem_content_type_id_object_id_tag_id_4bb97a8e_uniq" ON "taggit_taggeditem" ("content_type_id", "object_id", "tag_id");
CREATE TABLE IF NOT EXISTS "taggit_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "slug" varchar(100) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "djbooks_address" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "names" varchar(20) NOT NULL, "last_names" varchar(20) NOT NULL, "phone" varchar(20) NOT NULL, "email" varchar(20) NOT NULL, "street_address" varchar(100) NOT NULL, "shipping_country" varchar(100) NOT NULL, "shipping_city" varchar(100) NOT NULL, "shipping_zip" varchar(100) NOT NULL, "address_type" varchar(1) NOT NULL, "default" bool NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_book" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(100) NOT NULL, "author" varchar(30) NOT NULL, "editorial" varchar(30) NOT NULL, "edition" varchar(20) NOT NULL, "year" varchar(4) NOT NULL, "price" real NOT NULL, "discount_price" real NULL, "cover" varchar(100) NOT NULL, "back" varchar(100) NULL, "description" text NULL, "condition" text NULL, "stock" integer NOT NULL, "slug" varchar(255) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "djbooks_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(40) NOT NULL, "image" varchar(100) NULL, "slug" varchar(40) NOT NULL);
CREATE TABLE IF NOT EXISTS "djbooks_payment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "charge_id" varchar(50) NOT NULL, "amount" real NOT NULL, "timestamp" datetime NOT NULL, "payment_method" varchar(2) NOT NULL, "user_id" integer NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_orderbook" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ordered" bool NOT NULL, "quantity" integer NOT NULL, "item_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_order" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ref_code" varchar(20) NULL, "start_date" datetime NOT NULL, "ordered_date" datetime NOT NULL, "paid" bool NOT NULL, "ordered" bool NOT NULL, "being_delivered" bool NOT NULL, "received" bool NOT NULL, "shipping_option" varchar(12) NULL, "shipping_address_id" bigint NULL REFERENCES "djbooks_address" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_order_items" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "order_id" bigint NOT NULL REFERENCES "djbooks_order" ("id") DEFERRABLE INITIALLY DEFERRED, "orderbook_id" bigint NOT NULL REFERENCES "djbooks_orderbook" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_extraimage" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "image" varchar(100) NOT NULL, "book_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_book_category" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "book_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED, "category_id" bigint NOT NULL REFERENCES "djbooks_category" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "djbooks_book_related_books" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "from_book_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED, "to_book_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "djbooks_address_user_id_747c892f" ON "djbooks_address" ("user_id");
CREATE INDEX "djbooks_category_slug_46586ef7" ON "djbooks_category" ("slug");
CREATE INDEX "djbooks_payment_user_id_db5e94ff" ON "djbooks_payment" ("user_id");
CREATE INDEX "djbooks_orderbook_item_id_62c63387" ON "djbooks_orderbook" ("item_id");
CREATE INDEX "djbooks_orderbook_user_id_9d623c28" ON "djbooks_orderbook" ("user_id");
CREATE INDEX "djbooks_order_shipping_address_id_8755941f" ON "djbooks_order" ("shipping_address_id");
CREATE INDEX "djbooks_order_user_id_c197a67c" ON "djbooks_order" ("user_id");
CREATE UNIQUE INDEX "djbooks_order_items_order_id_orderbook_id_3f8848be_uniq" ON "djbooks_order_items" ("order_id", "orderbook_id");
CREATE INDEX "djbooks_order_items_order_id_8692b152" ON "djbooks_order_items" ("order_id");
CREATE INDEX "djbooks_order_items_orderbook_id_dbfaad0d" ON "djbooks_order_items" ("orderbook_id");
CREATE INDEX "djbooks_extraimage_book_id_b72975ea" ON "djbooks_extraimage" ("book_id");
CREATE UNIQUE INDEX "djbooks_book_category_book_id_category_id_04f94de5_uniq" ON "djbooks_book_category" ("book_id", "category_id");
CREATE INDEX "djbooks_book_category_book_id_74e8f450" ON "djbooks_book_category" ("book_id");
CREATE INDEX "djbooks_book_category_category_id_a1458020" ON "djbooks_book_category" ("category_id");
CREATE UNIQUE INDEX "djbooks_book_related_books_from_book_id_to_book_id_d3dc6c86_uniq" ON "djbooks_book_related_books" ("from_book_id", "to_book_id");
CREATE INDEX "djbooks_book_related_books_from_book_id_a062a7dc" ON "djbooks_book_related_books" ("from_book_id");
CREATE INDEX "djbooks_book_related_books_to_book_id_4d480620" ON "djbooks_book_related_books" ("to_book_id");
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
CREATE TABLE IF NOT EXISTS "django_site" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "domain" varchar(100) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "socialaccount_socialapp_sites" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "socialapp_id" integer NOT NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED, "site_id" integer NOT NULL REFERENCES "django_site" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "socialaccount_socialtoken" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "token" text NOT NULL, "token_secret" text NOT NULL, "expires_at" datetime NULL, "account_id" integer NOT NULL REFERENCES "socialaccount_socialaccount" ("id") DEFERRABLE INITIALLY DEFERRED, "app_id" integer NOT NULL REFERENCES "socialaccount_socialapp" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq" ON "socialaccount_socialtoken" ("app_id", "account_id");
CREATE UNIQUE INDEX "socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq" ON "socialaccount_socialapp_sites" ("socialapp_id", "site_id");
CREATE INDEX "socialaccount_socialapp_sites_socialapp_id_97fb6e7d" ON "socialaccount_socialapp_sites" ("socialapp_id");
CREATE INDEX "socialaccount_socialapp_sites_site_id_2579dee5" ON "socialaccount_socialapp_sites" ("site_id");
CREATE INDEX "socialaccount_socialtoken_account_id_951f210e" ON "socialaccount_socialtoken" ("account_id");
CREATE INDEX "socialaccount_socialtoken_app_id_636a42d7" ON "socialaccount_socialtoken" ("app_id");
CREATE TABLE IF NOT EXISTS "socialaccount_socialapp" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "provider" varchar(30) NOT NULL, "name" varchar(40) NOT NULL, "client_id" varchar(191) NOT NULL, "key" varchar(191) NOT NULL, "secret" varchar(191) NOT NULL);
CREATE TABLE IF NOT EXISTS "socialaccount_socialaccount" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "provider" varchar(30) NOT NULL, "uid" varchar(191) NOT NULL, "last_login" datetime NOT NULL, "date_joined" datetime NOT NULL, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "extra_data" text NOT NULL);
CREATE UNIQUE INDEX "socialaccount_socialaccount_provider_uid_fc810c6e_uniq" ON "socialaccount_socialaccount" ("provider", "uid");
CREATE INDEX "socialaccount_socialaccount_user_id_8146e70c" ON "socialaccount_socialaccount" ("user_id");
CREATE TABLE IF NOT EXISTS "djbooks_book_users_wishlist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "book_id" bigint NOT NULL REFERENCES "djbooks_book" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE UNIQUE INDEX "djbooks_book_users_wishlist_book_id_user_id_d28d7ca4_uniq" ON "djbooks_book_users_wishlist" ("book_id", "user_id");
CREATE INDEX "djbooks_book_users_wishlist_book_id_435fda3d" ON "djbooks_book_users_wishlist" ("book_id");
CREATE INDEX "djbooks_book_users_wishlist_user_id_338f287d" ON "djbooks_book_users_wishlist" ("user_id");
CREATE INDEX "djbooks_book_users_wishlist_user_id_338f287d" ON "djbooks_book_users_wishlist" ("user_id");