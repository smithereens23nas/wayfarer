
INSERT INTO main_app_city(name, img, description)
    VALUES('Miami','https://mmimageservice.azurewebsites.net/api/image/office/039','Miami, officially the City of Miami, is a coastal metropolis located in Miami-Dade County in southeastern Florida. With a population of 467,963 as of the 2020 census, it is the 44th-largest city in the United States and the core of the nation''s eighth-largest metropolitan area.','1');
INSERT INTO main_app_city(name, img, description)
    VALUES('Los Angles','https://a.cdn-hotels.com/gdcs/production104/d87/607b5514-cc8b-4db2-a40b-8087b6dd9135.jpg','Los Angeles is a sprawling Southern California city and the center of the nation''s film and television industry. Near its iconic Hollywood sign, studios such as Paramount Pictures, Universal and Warner Brothers offer behind-the-scenes tours. On Hollywood Boulevard, TCL Chinese Theatre displays celebrities hand- and footprints, the Walk of Fame honors thousands of luminaries and vendors sell maps to stars homes');
INSERT INTO main_app_city(name, img, description)
    VALUES('New York','https://www.history.com/.image/ar_1:1%2Cc_fill%2Ccs_srgb%2Cfl_progressive%2Cq_auto:good%2Cw_1200/MTU3ODc5MDgyNjY5OTc1MjYz/new-york-city.jpg','New York City comprises 5 boroughs sitting where the Hudson River meets the Atlantic Ocean. At its core is Manhattan, a densely populated borough that''s among the world''s major commercial, financial and cultural centers. Its iconic sites include skyscrapers such as the Empire State Building and sprawling Central Park. Broadway theater is staged in neon-lit Times Square.');
INSERT INTO main_app_city(name, img, description)
    VALUES('Rio de Janiero','https://static1.evcdn.net/images/reduction/1253999_w-1200_h-630_q-70_m-crop.jpg','Rio de Janeiro is a huge seaside city in Brazil, famed for its Copacabana and Ipanema beaches, 38m Christ the Redeemer statue atop Mount Corcovado and for Sugarloaf Mountain, a granite peak with cable cars to its summit. The city is also known for its sprawling favelas (shanty towns). Its raucous Carnaval festival, featuring parade floats, flamboyant costumes and samba dancers, is considered the world''s largest');
INSERT INTO main_app_city(name, img, description)
    VALUES('Brasilia','https://ychef.files.bbci.co.uk/976x549/p0216mjh.jpg','Brasília, inaugurated as capital of Brazil in 1960, is a planned city distinguished by its white, modern architecture, chiefly designed by Oscar Niemeyer. Laid out in the shape of an airplane, its “fuselage” is the Monumental Axis, 2 wide avenues flanking a massive park. In the “cockpit” is Praça dos Três Poderes, named for the 3 branches of government surrounding it');
INSERT INTO main_app_city(name, img, description)
    VALUES('Sao Paulo','https://assets.tivolihotels.com/image/upload/q_auto,f_auto/media/minor/tivoli/images/destination/saopaulo/thr_top_saopaulo_1920x1000.jpg','São Paulo, Brazil''s vibrant financial center, is among the world''s most populous cities, with numerous cultural institutions and a rich architectural tradition. Its iconic buildings range from its neo-Gothic cathedral and the 1929 Martinelli skyscraper to modernist architect Oscar Niemeyer''s curvy Edifício Copan. The colonial-style Pátio do Colégio church marks where Jesuit priests founded the city in 1554.');



INSERT INTO main_app_post('title','city', 'img', 'body','author')
    VALUES('first post','Sao Paulo','https://assets.tivolihotels.com/image/upload/q_auto,f_auto/media/minor/tivoli/images/destination/saopaulo/thr_top_saopaulo_1920x1000.jpg','words words words','Michealangelo');

INSERT INTO main_app_post('title','city', 'img', 'body','author')
    VALUES('second post','New York','https://cdn.cheapoguides.com/wp-content/uploads/sites/3/2019/03/Osaka-castle-cherry-blosson-iStock-512491222.jpg','Florence, capital of Italy''s Tuscany region, is home to many masterpieces of Renaissance art and architecture. One of its most iconic sights is the Duomo, a cathedral with a terracotta-tiled dome engineered by Brunelleschi and a bell tower by Giotto. The Galleria dell''Accademia displays Michelangelo''s “David” sculpture. The Uffizi Gallery exhibits Botticelli''s “The Birth of Venus” and da Vinci''s “Annunciation.”','SamSmith');

INSERT INTO main_app_post('title','city', 'img', 'body','author')
    VALUES('other post','Sao Paulo','https://cdn.cheapoguides.com/wp-content/uploads/sites/3/2019/03/Osaka-castle-cherry-blosson-iStock-512491222.jpg','Venice, the capital of northern Italy''s Veneto region, is built on more than 100 small islands in a lagoon in the Adriatic Sea. It has no roads, just canals – including the Grand Canal thoroughfare – lined with Renaissance and Gothic palaces. The central square, Piazza San Marco, contains St. Mark''s Basilica, which is tiled with Byzantine mosaics, and the Campanile bell tower offering views of the city''s red roofs.','Raphael');

INSERT INTO main_app_post('title','city', 'img', 'body','author')
    VALUES('more post','Rio de Janiero','https://cdn.cheapoguides.com/wp-content/uploads/sites/3/2019/03/Osaka-castle-cherry-blosson-iStock-512491222.jpg','Tokyo, Japan''s busy capital, mixes the ultramodern and the traditional, from neon-lit skyscrapers to historic temples. The opulent Meiji Shinto Shrine is known for its towering gate and surrounding woods. The Imperial Palace sits amid large public gardens. The city''s many museums offer exhibits ranging from classical art (in the Tokyo National Museum) to a reconstructed kabuki theater (in the Edo-Tokyo Museum).','NickSmith');


INSERT INTO main_app_profile(user, name, email, city, profile_pic)
    VALUES('jimmy','fake_email','Kyoto','https://kyoto-amc.iafor.org/wp-content/uploads/sites/55/2017/01/The-Kyoto-Conference-on-Arts-Media-Culture-7.jpg',);
INSERT INTO main_app_profile(user, name, email, city, profile_pic)
    VALUES('johny','anemail','Osaka','https://cdn.cheapoguides.com/wp-content/uploads/sites/3/2019/03/Osaka-castle-cherry-blosson-iStock-512491222.jpg');
INSERT INTO main_app_profile(user, name, email, city, profile_pic)
    VALUES('nick','anotheremail','Kingston','https://idbinvest.org/sites/default/files/styles/size936x656/public/blog_post/A_View_Of_The_Skyline_In_Kingston_Jamaica-d.jpg.webp?itok=R8MgAD7K');
INSERT INTO main_app_profile(user, name, email, city, profile_pic)
    VALUES('some guy in his mom''s basement','anotheremail again','Montego Bay','https://www.sunsetmontegobay.com/images/slides/slide-11.jpg');
