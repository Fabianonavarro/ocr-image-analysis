import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import face_recognition
import progressbar  # Importando a biblioteca progressbar2

# Função para detectar rostos usando a biblioteca face_recognition
def detectar_faces(imagem_path):
    imagem = face_recognition.load_image_file(imagem_path)
    face_locations = face_recognition.face_locations(imagem)
    return face_locations

# Função para detectar objetos usando OpenCV (usando classificador Haar)
def detectar_objetos(imagem_path):
    imagem = cv2.imread(imagem_path)
    
    # Carregar o classificador Haar (para detecção de rostos)
    objeto_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    objetos = objeto_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    objetos_detectados = []
    for (x, y, w, h) in objetos:
        # Para fins de exemplo, vamos detectar "rostos" (ou qualquer objeto detectado)
        objetos_detectados.append("Rosto")
    
    return objetos_detectados

# Função para gerar imagem com dados sobrepostos
def gerar_imagem_com_texto(imagem_path, faces, objetos, saida_path):
    imagem = Image.open(imagem_path)
    draw = ImageDraw.Draw(imagem)
    font = ImageFont.load_default()
    
    texto = f"Faces detectadas: {len(faces)} | Objetos: {', '.join(objetos)}"
    draw.text((10, 10), texto, fill=(255, 255, 255), font=font)
    
    # Desenhando os rostos detectados na imagem
    for (top, right, bottom, left) in faces:
        draw.rectangle([left, top, right, bottom], outline="yellow", width=2)
    
    imagem.save(saida_path)
    print(f"Imagem processada salva como {saida_path}")

# Função para gerar arquivo de texto com informações
def gerar_arquivo_texto(imagem_path, faces, objetos):
    nome_arquivo = os.path.join("output", "info_" + os.path.basename(imagem_path).replace('.jpg', '.txt'))
    os.makedirs(os.path.dirname(nome_arquivo), exist_ok=True)  # Cria a pasta output se não existir
    with open(nome_arquivo, 'w') as f:
        f.write(f"Imagem: {imagem_path}\n")
        f.write(f"Quantidade de rostos detectados: {len(faces)}\n")
        f.write(f"Objetos detectados: {', '.join(objetos)}\n")
    print(f"Arquivo de informações salvo como {nome_arquivo}")

# Função para escolher imagens da pasta "inputs"
def escolher_imagem_da_pasta(pasta):
    imagens = [f for f in os.listdir(pasta) if f.endswith(('jpg', 'jpeg', 'png'))]
    if not imagens:
        print("Nenhuma imagem disponível na pasta!")
        return None
    return [os.path.join(pasta, img) for img in imagens]

# Função principal
def main():
    pasta_imagens = "inputs"
    imagens = escolher_imagem_da_pasta(pasta_imagens)
    if not imagens:
        return
    
    os.makedirs("output", exist_ok=True)  # Cria a pasta de saída caso não exista

    # Perguntar ao usuário se quer processar uma imagem ou todas
    escolha = input("Digite 1 para escolher uma imagem ou 2 para processar todas as imagens: ")

    if escolha == "1":
        # Mostrar as imagens disponíveis para o usuário escolher
        print("Escolha uma imagem para processar:")
        for idx, imagem in enumerate(imagens, 1):
            print(f"{idx} - {os.path.basename(imagem)}")
        
        try:
            imagem_escolhida_idx = int(input("Digite o número da imagem que você deseja processar: "))
            if 1 <= imagem_escolhida_idx <= len(imagens):
                imagem_escolhida = imagens[imagem_escolhida_idx - 1]
                imagens = [imagem_escolhida]
            else:
                print("Número inválido. Saindo.")
                return
        except ValueError:
            print("Opção inválida. Saindo.")
            return

    elif escolha == "2":
        print("Processando todas as imagens na pasta.")
    else:
        print("Escolha inválida!")
        return
    
    # Inicializando a barra de progresso
    bar = progressbar.ProgressBar(widgets=[
        ' [', progressbar.Percentage(), '] ',
        progressbar.Bar(), ' ',
        progressbar.ETA()], maxval=len(imagens)).start()

    # Processando as imagens
    for i, imagem_path in enumerate(imagens):
        print(f"Processando: {imagem_path}")
        
        # Detectar rostos usando face_recognition
        faces = detectar_faces(imagem_path)
        
        # Detectar objetos (usando OpenCV aqui com o classificador Haar)
        objetos_detectados = detectar_objetos(imagem_path)
        
        # Gerar a imagem com texto sobreposto
        nome_saida = os.path.join("output", "resultado_" + os.path.basename(imagem_path))
        gerar_imagem_com_texto(imagem_path, faces, objetos_detectados, nome_saida)
        
        # Gerar o arquivo de texto com informações
        gerar_arquivo_texto(imagem_path, faces, objetos_detectados)

        # Atualizando a barra de progresso
        bar.update(i + 1)

    # Finalizando a barra de progresso
    bar.finish()

if __name__ == "__main__":
    main()
