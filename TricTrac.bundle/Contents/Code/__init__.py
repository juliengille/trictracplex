TITLE = 'Tric Trac'
ART = 'art-default.jpeg'
ICON = 'icon-default.png'
#ESPN_LIVE = "http://espn.go.com/watchespn/feeds/startup?action=live&channel=%s"
#ESPN_PLAYER = "http://espn.go.com/watchespn/player/_/id/%s?hd=%s"

TRICTRAC_INFO = "http://www.trictrac.net/medias/les-videos/les-videos/boxes500/1/32"
TRICTRAC_INFO2 = "http://www.trictrac.net/medias/les-videos/les-videos/boxes500/2/32"
TRICTRAC_INFO3 = "http://www.trictrac.net/medias/les-videos/les-videos/boxes500/3/32"
TRICTRAC_INFO4 = "http://www.trictrac.net/medias/les-videos/les-videos/boxes500/4/32"
TRICTRAC_INFO5 = "http://www.trictrac.net/medias/les-videos/les-videos/boxes500/5/32"

TRICTRAC_URL="http://trictrac.tv"

TRICTRAC_SEARCH="http://trictrac.tv/home/listing.php?mot="

#TRICTRAC_INFOS= [TRICTRAC_INFO, TRICTRAC_INFO2, TRICTRAC_INFO3, TRICTRAC_INFO4,TRICTRAC_INFO5]
TRICTRAC_INFOS= [TRICTRAC_INFO, TRICTRAC_INFO2]

####################################################################################################
def Start():

    Plugin.AddPrefixHandler('/video/trictrac', Menu, TITLE, ICON, ART)
    Plugin.AddViewGroup('InfoList', viewMode='InfoList', mediaType='items')

    ObjectContainer.title1 = TITLE
    ObjectContainer.art = R(ART)
    ObjectContainer.view_group = 'InfoList'

    DirectoryObject.thumb = R(ICON)
    DirectoryObject.art = R(ART)
    InputDirectoryObject.thumb = R(ICON)
    InputDirectoryObject.art = R(ART)
    VideoClipObject.thumb = R(ICON)

####################################################################################################
def Menu():
    oc = ObjectContainer()
    oc.add(DirectoryObject(key = Callback(MainMenu), title = 'Last'))
    oc.add(InputDirectoryObject(key = Callback(Search), title = 'Recherche',prompt = 'Nom de la video'))
    return oc


####################################################################################################
@route('/video/trictrac/search', allow_sync=True)
def Search(query='robinson'):
    Log("Search for "+query)

    oc = ObjectContainer()

    data = HTML.ElementFromURL(TRICTRAC_SEARCH+String.Quote(query));  
    videos = data.xpath("//ul[@id='Commentaires']/li")

    for video in videos:
            video_url = TRICTRAC_URL+video.xpath(".//a")[0].attrib['href']
            Log('Video URL '+video_url)
            video_title = video.xpath(".//div[@id='titlesearch']/span")[0].text
            Log('Video Title '+video_title)
            video_thumb = TRICTRAC_URL+video.xpath(".//div[@id='imgsearch']/img/@src")[0]
            Log('Video Thumb '+video_thumb)

            oc.add(VideoClipObject(
                url = video_url,
                title = video_title,
                thumb = Resource.ContentsOfURLWithFallback(video_thumb, fallback=ICON)))

    return oc    

@route('/video/trictrac/last', allow_sync=True)
def MainMenu():

#    oc = ObjectContainer()
#    oc.add(DirectoryObject(key = Callback(GetEvents, title = "test"), title = 'test'))
#    return oc

    oc = ObjectContainer()
#    hd = 0

#    if Client.Platform in ['Windows', 'MacOSX', 'Linux']:
#        hd = 1

#    for item in XML.ElementFromURL(ESPN_LIVE % (title), cacheTime=300).xpath('//events/event'):
#        item_title = item.xpath('./name')[0].text
#        league = item.xpath('./league')[0].text
#        oc.add(VideoClipObject(
#            url = ESPN_PLAYER % (item.get('id'), hd),
#            title = (league + " - " + item_title) if league != "" else (item_title),
#            summary = item_title,
#            thumb = Resource.ContentsOfURLWithFallback(url=item.xpath('./thumbnail/large')[0].text, fallback=ICON)))


# Retrieve info

    # Read file


    for info in TRICTRAC_INFOS:
        data = HTML.ElementFromURL(info);
        videos = data.xpath("//div[@class='medias_box']")

        for video in videos:
    #    for index in range(0,3):
    #        video = videos[index]
            video_url = video.xpath(".//h2/a")[0].attrib['href']
            Log('Video URL '+video_url)
            video_title = video.xpath(".//h2/a")[0].attrib['title']
            Log('Video Title '+video_title)
            video_thumb = video.xpath(".//div[@class='image']/a/img/@src")[0]
            Log('Video Thumb '+video_thumb)

            oc.add(VideoClipObject(
                url = video_url,
                title = video_title,
                thumb = Resource.ContentsOfURLWithFallback(video_thumb, fallback=ICON)))

#    url = "http://trictrac.tv/video-le-fantome-de-l-opera-de-l-explication"
#    data = HTML.ElementFromURL(url);
#    idAtt = data.xpath("//div[@id='Content_Video']/object/param[@name='flashvars']")
#    Log('ID ?')
#    id=idAtt[0].attrib['value']
#    Log(id)
#    number = Regex('varplaymedia=([0-9]*)&').search(id).group(1)
#    Log('-- number')
#    Log(number)

#    Log("Retrieve http://www.trictrac.tv/swf/listelement.php?idfile="+number)

#    request = HTTP.Request("http://www.trictrac.tv/swf/listelement.php?idfile="+number)
#    request.load();
#    Log("Request result--")
#    Log(request.content)

#    DESC=Regex("&fichier=(.*)&descriptif=(.*)&titre=(.*)&idcode=")
#    fichier=DESC.search(request.content).group(1)
#    desc=DESC.search(request.content).group(2).replace('+',' ')  
#    titre=DESC.search(request.content).group(3).replace('+',' ')  

#    desc=String.Unquote(desc)
#    titre=String.Unquote(titre)

#    Log("[FICHIER] "+fichier)
#    Log("[DESC] "+desc)
#    Log("[TITRE] "+titre)

#    Log('Media object for url '+url)

#    oc.add(VideoClipObject(
#        url = url,
#        title = titre,
#        summary = desc,
#        thumb = Resource.ContentsOfURLWithFallback("http://trictrac.tv/miseenavant/video_1377273097.jpg", fallback=ICON)))


    return oc


####################################################################################################
@route('/video/trictrac/getevents')
def GetEvents(title):

    oc = ObjectContainer()
#    hd = 0

#    if Client.Platform in ['Windows', 'MacOSX', 'Linux']:
#        hd = 1

#    for item in XML.ElementFromURL(ESPN_LIVE % (title), cacheTime=300).xpath('//events/event'):
#        item_title = item.xpath('./name')[0].text
#        league = item.xpath('./league')[0].text
#        oc.add(VideoClipObject(
#            url = ESPN_PLAYER % (item.get('id'), hd),
#            title = (league + " - " + item_title) if league != "" else (item_title),
#            summary = item_title,
#            thumb = Resource.ContentsOfURLWithFallback(url=item.xpath('./thumbnail/large')[0].text, fallback=ICON)))


# Retrieve info
    url = "http://trictrac.tv/video-le-fantome-de-l-opera-de-l-explication"
    data = HTML.ElementFromURL(url);
    idAtt = data.xpath("//div[@id='Content_Video']/object/param[@name='flashvars']")
    Log('ID ?')
    id=idAtt[0].attrib['value']
    Log(id)
    number = Regex('varplaymedia=([0-9]*)&').search(id).group(1)
    Log('-- number')
    Log(number)

    Log("Retrieve http://www.trictrac.tv/swf/listelement.php?idfile="+number)

    request = HTTP.Request("http://www.trictrac.tv/swf/listelement.php?idfile="+number)
    request.load();
    Log("Request result--")
    Log(request.content)

    DESC=Regex("&fichier=(.*)&descriptif=(.*)&titre=(.*)&idcode=")
    fichier=DESC.search(request.content).group(1)
    desc=DESC.search(request.content).group(2).replace('+',' ')  
    titre=DESC.search(request.content).group(3).replace('+',' ')  

    desc=String.Unquote(desc)
    titre=String.Unquote(titre)

    Log("[FICHIER] "+fichier)
    Log("[DESC] "+desc)
    Log("[TITRE] "+titre)

    Log('Media object for url '+url)

    oc.add(VideoClipObject(
#        url = "http://trictrac.tv/video-robinson-crusoe-de-la-partie",
        url = url,
        title = titre,
        summary = desc,
        thumb = Resource.ContentsOfURLWithFallback("http://trictrac.tv/miseenavant/video_1377273097.jpg", fallback=ICON)))


    return oc

####################################################################################################